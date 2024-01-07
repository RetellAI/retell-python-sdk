import asyncio
import websockets
import json
from typing import List, Callable, Dict
from .models.components import agentpromptparams
import urllib.parse

class EventEmitter:
    def __init__(self):
        self.callbacks: Dict[str, List[Callable]] = {}

    def on(self, event: str, callback: Callable):
        if event not in self.callbacks:
            self.callbacks[event] = []
        self.callbacks[event].append(callback)

    def emit(self, event: str, *args):
        if event in self.callbacks:
            for callback in self.callbacks[event]:
                callback(*args)

class LiveClient(EventEmitter):
    def __init__(self, api_key: str, agent_id: str, sample_rate: int,
                 agent_prompt_params: List[agentpromptparams.AgentPromptParams], base_endpoint: str):
        super().__init__()

        self.endpoint = (f"{base_endpoint}/create-web-call?api_key={api_key}"
                    f"&agent_id={agent_id}&sample_rate={sample_rate}")
        param_list = []
        for param in agent_prompt_params:
            param_list.append({"name": param.name, "value": param.value})
        self.endpoint += "&agent_prompt_params=" + urllib.parse.quote(json.dumps(param_list))
                
    async def wait_for_ready(self):
        except_raised = False
        try:
            self.ws = await websockets.connect(self.endpoint)
            async for message in self.ws:
                data = json.loads(message)
                if data['status'] == 'ready':
                    self.call = data['call']
                    asyncio.create_task(self.__receive_audio())
                    return
                else:
                    self.ws.close()
                    raise Exception("Event other than ready received first")
        except Exception as e:
            if hasattr(self, "ws") and self.ws.open:
                self.ws.close()
            except_raised = True
            raise Exception(e)
        finally:
            if hasattr(self, "ws") and self.ws.closed and not except_raised:
                raise Exception("Websocket closed before ready")
            
    async def __receive_audio(self):
        try:
            async for message in self.ws:
                self.emit('audio', message)
        except websockets.ConnectionClosedError as e:
            self.emit('error', e)
        except Exception as e:
            self.emit('error', e)
        finally:
            self.emit('close')
                     
    async def send(self, audio: bytes):
        if hasattr(self, "ws") and self.ws.open:
            await self.ws.send(audio)

    async def close(self):
        await self.ws.close()
    
    def get_call(self):
       return self.call