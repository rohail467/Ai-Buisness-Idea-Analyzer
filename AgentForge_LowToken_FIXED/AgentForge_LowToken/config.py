import os

# Fix CrewAI 1.15.x + Groq cache_breakpoint compatibility issue.
# CrewAI adds an Anthropic-specific cache marker that Groq rejects.
try:
    import crewai.llms.cache as crewai_cache

    crewai_cache.mark_cache_breakpoint = lambda message: message
except Exception:
    pass

from crewai import LLM


MODEL = "openai/gpt-oss-120b"


def make_llm(max_tokens: int):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is not configured.")

    return LLM(
        model=f"groq/{MODEL}",
        api_key=api_key,
        temperature=0.2,
        max_tokens=max_tokens,
        reasoning_effort="low",
        timeout=120,
    )
