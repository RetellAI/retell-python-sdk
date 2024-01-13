import pyaudio
import queue
import asyncio
from retellclient.sdk import RetellClient
from retellclient.models import components, operations

api_key = "YOUR_API_KEY"
agent_id = "YOUR_AGENT_ID"
sample_rate = 24000
close_audio = False

class AudioModule:
    def __init__(self):
        self.audio_format = pyaudio.paInt16
        self.channels = 1
        self.rate = sample_rate
        self.chunk = 1024
        self.pyaudio_instance = pyaudio.PyAudio()

        self.capture_queue = queue.Queue()

        def mic_audio_callback(in_data, frame_count, time_info, status):
            self.capture_queue.put(in_data)
            return (None, pyaudio.paContinue)

        self.stream = self.pyaudio_instance.open(format=self.audio_format,
                                                 channels=self.channels,
                                                 rate=self.rate,
                                                 input=True,
                                                 frames_per_buffer=self.chunk,
                                                 stream_callback=mic_audio_callback)
        self.output_stream = self.pyaudio_instance.open(format=self.audio_format,
                                                        channels=self.channels,
                                                        rate=self.rate,
                                                        output=True)


    def get_audio_chunk(self):
        if not self.capture_queue.empty():
            return self.capture_queue.get()
        return None

    def play_audio(self, data):
        self.output_stream.write(data)

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.output_stream.stop_stream()
        self.output_stream.close()
        self.pyaudio_instance.terminate()


async def main():
    global close_audio
    # Initialize your LiveClient with appropriate parameters
    client = RetellClient(api_key = api_key)
    params = operations.CreateWebCallParams(
        agent_id=agent_id,
        sample_rate = sample_rate,
        agent_prompt_params=[
        components.AgentPromptParams(
            name='username',
            value='Adam',
        ),
    ])
    live_client = await client.create_web_call(params)

    audio_module = AudioModule()

    def on_audio_received(message):
        audio_module.play_audio(message)
    def on_error_received(message):
        print("error", message)
    def on_close_received():
        global close_audio
        print("websocket closed")
        audio_module.close()
        close_audio = True

    live_client.on("audio", on_audio_received)
    live_client.on("error", on_error_received)
    live_client.on("close", on_close_received)

    while not close_audio:
        # Check for new audio chunk and send it
        audio_chunk = audio_module.get_audio_chunk()
        if audio_chunk:
            await live_client.send(audio_chunk)
        await asyncio.sleep(0) # Yield control to allow other async operations


if __name__ == "__main__":
    asyncio.run(main())
