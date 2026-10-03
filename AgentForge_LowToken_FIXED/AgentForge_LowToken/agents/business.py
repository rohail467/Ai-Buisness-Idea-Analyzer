from crewai import Agent

def create_business_agent(llm):
    return Agent(
        role="Business Strategist",
        goal="Find a realistic value proposition, revenue path, acquisition idea and business risks.",
        backstory="Practical startup strategist. Avoid unsupported revenue claims.",
        llm=llm, verbose=False, allow_delegation=False, max_iter=1,
    )
