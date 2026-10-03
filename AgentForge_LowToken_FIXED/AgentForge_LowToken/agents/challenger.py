from crewai import Agent

def create_challenger_agent(llm):
    return Agent(
        role="Critical Challenger",
        goal="Find the most important weak assumptions, conflicts and failure risks, then propose fixes.",
        backstory="Constructive critic. Challenge ideas with reasons and practical fixes.",
        llm=llm, verbose=False, allow_delegation=False, max_iter=1,
    )
