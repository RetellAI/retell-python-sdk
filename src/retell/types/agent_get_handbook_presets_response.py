# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AgentGetHandbookPresetsResponse"]


class AgentGetHandbookPresetsResponse(BaseModel):
    ai_disclosure: str

    conversational: str

    customer_support: str

    echo_verification: str

    high_empathy: str

    nato_phonetic_alphabet: str

    natural_filler_words: str

    scope_boundaries: str

    smart_matching: str

    speech_normalization: str
