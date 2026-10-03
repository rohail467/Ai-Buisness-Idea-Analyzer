from crewai import Task

def debate_task(agent, market, business, technical):
    return Task(
        description="""Challenge the three specialist analyses for: {idea}

The previous Market, Business, and Technical task outputs are provided through
CrewAI context. Do NOT ask for them as input variables.

Return ONLY:
Biggest weakness:
Conflicting point:
Customer objection:
Business objection:
Technical objection:
Fixes:

Use short, concrete points. Do not invent facts.""",
        expected_output="Six concise challenge fields.",
        agent=agent,
        context=[market, business, technical],
    )
