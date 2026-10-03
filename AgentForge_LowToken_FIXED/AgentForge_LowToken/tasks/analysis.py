from crewai import Task

def market_task(agent):
    return Task(
        description="""Analyze this idea: {idea}
Return ONLY:
Customers:
Problem:
Alternatives:
Opportunity:
Top risks:
Assumptions:
Keep each field to 1-2 short sentences. No invented statistics or live-research claims.""",
        expected_output="Six concise labeled fields.",
        agent=agent,
    )

def business_task(agent):
    return Task(
        description="""Analyze this idea: {idea}
Return ONLY:
Value:
Revenue:
Acquisition:
Opportunity:
Top risks:
Keep each field to 1-2 short sentences. No unsupported numbers.""",
        expected_output="Five concise labeled fields.",
        agent=agent,
    )

def technical_task(agent):
    return Task(
        description="""Evaluate this idea: {idea}
Return ONLY:
MVP:
Stack:
Components:
AI:
Top risks:
Keep each field to 1-2 short sentences. Prefer simple implementation.""",
        expected_output="Five concise labeled fields.",
        agent=agent,
    )
