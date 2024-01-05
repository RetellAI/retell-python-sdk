"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import agent as components_agent
from ...models.components import agentnodefaultnorequired as components_agentnodefaultnorequired
from typing import Optional


@dataclasses.dataclass
class UpdateAgentRequest:
    agent_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'agent_id', 'style': 'simple', 'explode': False }})
    r"""Unique id of the agent to be updated."""
    agent_no_default_no_required: components_agentnodefaultnorequired.AgentNoDefaultNoRequired = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateAgentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    agent: Optional[components_agent.Agent] = dataclasses.field(default=None)
    r"""Successfully updated an agent."""
    

