import os
import streamlit as st

from crew.agentforge_crew import run_agentforge
from utils.ui import show_agent_status, show_debate, show_final_plan

st.set_page_config(page_title="AgentForge", page_icon="🚀", layout="wide")

def get_api_key():
    key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY", ""))
    if not key:
        raise ValueError("GROQ_API_KEY is missing. Add it in Streamlit Secrets.")
    os.environ["GROQ_API_KEY"] = key
    return key

st.title("🚀 AgentForge")
st.caption("AI Co-Founder: analyze → challenge → improve")

idea = st.text_area(
    "💡 Your startup / product / business idea",
    placeholder="Example: An AI tool that helps small restaurants reduce food waste.",
    height=130,
)

if st.button("🚀 Analyze My Idea", type="primary", use_container_width=True):
    if len(idea.strip()) < 10:
        st.warning("Please describe the idea in at least a few words.")
        st.stop()

    try:
        get_api_key()
    except ValueError as e:
        st.error(str(e))
        st.stop()

    status_box = st.empty()
    show_agent_status(
        status_box,
        {"Manager":"Waiting","Market":"Working","Business":"Working",
         "Technical":"Working","Challenger":"Waiting"},
    )

    try:
        result = run_agentforge(idea.strip(), status_box)
    except Exception as e:
        st.error("Analysis failed. Check the Groq key and Streamlit logs.")
        st.exception(e)
        st.stop()

    show_agent_status(
        status_box,
        {"Manager":"Completed","Market":"Completed","Business":"Completed",
         "Technical":"Completed","Challenger":"Completed"},
    )

    with st.expander("🔎 Market Analysis", expanded=False):
        st.markdown(result["market"])
    with st.expander("💰 Business Analysis", expanded=False):
        st.markdown(result["business"])
    with st.expander("💻 Technical Analysis", expanded=False):
        st.markdown(result["technical"])

    show_debate(result["debate"])
    show_final_plan(result["final"])
