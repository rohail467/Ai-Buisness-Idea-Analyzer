from crewai import Agent

def create_market_agent(llm):
    return Agent(
        role="Market Analyst",
        goal="Identify customer, problem, alternatives, opportunity and market risks.",
        backstory="Practical analyst. Never invent statistics or claim research you did not perform.",
        llm=llm, verbose=False, allow_delegation=False, max_iter=1,
    )
