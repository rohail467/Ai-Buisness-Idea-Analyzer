from crewai import Agent

def create_technical_agent(llm):
    return Agent(
        role="Technical Architect",
        goal="Define a simple MVP, stack, components, AI needs and technical risks.",
        backstory="MVP-focused architect. Prefer the simplest maintainable implementation.",
        llm=llm, verbose=False, allow_delegation=False, max_iter=1,
    )
