from crewai import Crew, Process

from config import make_llm
from agents.market import create_market_agent
from agents.business import create_business_agent
from agents.technical import create_technical_agent
from agents.challenger import create_challenger_agent
from agents.manager import create_manager_agent

from tasks.analysis import market_task, business_task, technical_task
from tasks.debate import debate_task
from tasks.final_plan import final_task

def _update(box, states):
    if box is not None:
        from utils.ui import show_agent_status
        show_agent_status(box, states)

def run_agentforge(idea, box=None):
    # Small-output LLM keeps the first four calls under a tight token budget.
    short_llm = make_llm(320)
    final_llm = make_llm(700)

    market = create_market_agent(short_llm)
    business = create_business_agent(short_llm)
    technical = create_technical_agent(short_llm)
    challenger = create_challenger_agent(short_llm)
    manager = create_manager_agent(final_llm)

    t_market = market_task(market)
    t_business = business_task(business)
    t_technical = technical_task(technical)
    t_debate = debate_task(challenger, t_market, t_business, t_technical)
    t_final = final_task(manager, t_market, t_business, t_technical, t_debate)

    crew = Crew(
        agents=[market, business, technical, challenger, manager],
        tasks=[t_market, t_business, t_technical, t_debate, t_final],
        process=Process.sequential,
        verbose=False,
    )

    result = crew.kickoff(inputs={"idea": idea})

    return {
        "market": t_market.output.raw if t_market.output else "",
        "business": t_business.output.raw if t_business.output else "",
        "technical": t_technical.output.raw if t_technical.output else "",
        "debate": t_debate.output.raw if t_debate.output else "",
        "final": result.raw if getattr(result, "raw", None) else str(result),
    }
