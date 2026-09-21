import os
from typing import Any

import anthropic
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment variables
# Override with MODEL=... in .env; default is the cheapest model
MODEL = os.getenv("MODEL", "claude-haiku-4-5-20251001")
_client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment


def call_model(
    messages: list[dict[str, Any]],
    system: str | None = None,
    tools: list[dict[str, Any]] | None = None,
    max_tokens: int = 400,
):
    """The ONLY place we talk to a model. Swap providers, add caching,
    cost tracking and tracing here later (Week 5)."""
    kwargs: dict[str, Any] = {
        "model": MODEL, "max_tokens": max_tokens, "messages": messages,
    }
    if system:
        kwargs["system"] = system
    if tools:
        kwargs["tools"] = tools
    return _client.messages.create(**kwargs)