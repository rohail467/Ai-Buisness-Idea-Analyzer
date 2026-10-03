from crewai import Agent

def create_manager_agent(llm):
    return Agent(
        role="Startup Team Manager",
        goal="Synthesize the analyses and debate into one concise, actionable improved plan.",
        backstory="Experienced startup manager. Resolve important conflicts and separate assumptions from facts.",
        llm=llm, verbose=False, allow_delegation=False, max_iter=1,
    )
