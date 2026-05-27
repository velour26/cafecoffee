"""Универсальный AI-клиент. Pollinations.ai по умолчанию (бесплатно, без ключа)."""

from __future__ import annotations

import os
from typing import Any

import httpx

AI_BASE_URL = os.getenv("AI_BASE_URL", "https://text.pollinations.ai/openai")
AI_API_KEY = os.getenv("AI_API_KEY", "").strip()
AI_MODEL = os.getenv("AI_MODEL", "openai")
AI_TIMEOUT = float(os.getenv("AI_TIMEOUT", "240"))


async def chat(
    messages: list[dict[str, str]],
    *,
    max_tokens: int = 600,
    temperature: float = 0.7,
) -> str:
    headers = {"Content-Type": "application/json"}
    if AI_API_KEY:
        headers["Authorization"] = f"Bearer {AI_API_KEY}"

    payload: dict[str, Any] = {
        "model": AI_MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

    async with httpx.AsyncClient(timeout=AI_TIMEOUT) as client:
        response = await client.post(AI_BASE_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()

    try:
        return (data["choices"][0]["message"]["content"] or "").strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected AI response shape: {data!r}") from exc
