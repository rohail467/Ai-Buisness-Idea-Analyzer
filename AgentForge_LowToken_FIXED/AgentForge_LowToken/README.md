# AgentForge — Low Token Edition

A simple Streamlit + CrewAI + Groq multi-agent startup analyzer.

## Design goals
- Groq only: `openai/gpt-oss-120b`
- No Serper API
- No Flask/FastAPI/Node/React
- Small prompts and capped outputs
- Five visible agents
- AI Debate before the final plan
- Works with any startup/product/business idea
- Designed for Streamlit Community Cloud

## Token-saving design
1. Specialist outputs are capped at 320 generated tokens.
2. Challenger output is also capped at 320.
3. Final manager gets 700 tokens.
4. GPT-OSS reasoning is set to `low`.
5. Agents have `max_iter=1` and delegation disabled, preventing unnecessary loops.
6. Prompts request only the fields needed by the next stage.
7. No web/search tool is required, so there is no Serper key.

This does not guarantee zero token-limit errors: actual usage also depends on the user's idea and CrewAI/LiteLLM overhead. The prompts are deliberately compact.

## Setup on Streamlit Cloud
Add this in Streamlit Secrets:

```toml
GROQ_API_KEY = "your_real_key"
```

Do NOT commit the real key to GitHub.

## Run
```bash
streamlit run app.py
```

## Important
The app does not claim to perform live market research. Market facts should be verified separately before making real business decisions.


## Important CrewAI fix
The debate and final tasks intentionally use `context=[...]` for earlier task outputs. They do not use `{market_output}`, `{business_output}`, `{technical_output}`, or `{debate_output}` because CrewAI treats those as kickoff template variables and raises a missing-variable error.
