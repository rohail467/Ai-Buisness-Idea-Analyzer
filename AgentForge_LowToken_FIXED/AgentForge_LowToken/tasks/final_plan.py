from crewai import Task

def final_task(agent, market, business, technical, debate):
    return Task(
        description="""Create the final improved plan for: {idea}

The previous Market, Business, Technical, and Challenger outputs are provided
through CrewAI context. Do NOT reference them as input variables.

Return ONLY these 10 headings:
1. Summary
2. Problem
3. Customers
4. Solution
5. Differentiator
6. Business Model
7. MVP
8. Technical Plan
9. Risks + Fixes
10. 90-Day Roadmap

Rules: concise; practical; no invented statistics; label assumptions;
apply useful fixes from the challenge.""",
        expected_output="A concise 10-section improved startup plan.",
        agent=agent,
        context=[market, business, technical, debate],
    )
