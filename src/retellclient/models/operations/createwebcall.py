from __future__ import annotations
import dataclasses
from ...models.components import agentpromptparams as components_agentpromptparams
from dataclasses_json import Undefined, dataclass_json
from retellclient import utils
from typing import List, Optional



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateWebCallParams:
    agent_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('agent_id') }})
    r"""Unique agent id to associate with this phone number."""
    sample_rate: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sample_rate') }})
    r"""Sample rate of input and output audio. Must be in range of [8000, 44100]."""
    agent_prompt_params: Optional[List[components_agentpromptparams.AgentPromptParams]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('agent_prompt_params'), 'exclude': lambda f: f is None }})
    r"""Supply values to your agent prompt parameters. If the given key value cannot match any param in prompt, it would have have any effect."""
    


