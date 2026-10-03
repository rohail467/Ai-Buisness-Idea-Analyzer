import os
from crewai import LLM

MODEL = "openai/gpt-oss-120b"

def make_llm(max_tokens: int):
    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise ValueError("GROQ_API_KEY is not configured.")

    return LLM(
        model=f"groq/{MODEL}",
        api_key=key,
        temperature=0.2,
        max_tokens=max_tokens,
        reasoning_effort="low",
        timeout=120,
    )
