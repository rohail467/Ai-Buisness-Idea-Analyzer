import streamlit as st

def show_agent_status(box, states):
    with box.container():
        st.subheader("🤖 AI Team")
        cols = st.columns(5)
        agents = [
            ("🧠", "Manager"), ("🔎", "Market"), ("💰", "Business"),
            ("💻", "Technical"), ("⚔️", "Challenger")
        ]
        for col, (icon, name) in zip(cols, agents):
            state = states.get(name, "Waiting")
            symbol = {"Completed":"🟢", "Working":"🟡", "Waiting":"⚪"}.get(state, "⚪")
            col.markdown(f"**{icon} {name}**<br>{symbol} {state}", unsafe_allow_html=True)

def show_debate(text):
    st.divider()
    st.subheader("⚔️ AI Debate")
    st.markdown(text)

def show_final_plan(text):
    st.divider()
    st.subheader("🚀 Improved Startup Plan")
    st.markdown(text)
