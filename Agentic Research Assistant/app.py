import streamlit as st
from agent import agent, new_thread

st.set_page_config(page_title="Research Agent", page_icon="🔬", layout="centered")

# ── Session State Init ──
if "thread" not in st.session_state:
    st.session_state.thread = new_thread()
if "query" not in st.session_state:
    st.session_state.query = ""
if "phase" not in st.session_state:
    st.session_state.phase = "input"
if "chat_threads" not in st.session_state:
    st.session_state.chat_threads = []  # list of {"query": ..., "thread": ...}

# ── SIDEBAR: Past Threads ──
st.sidebar.title("Past Research")
if not st.session_state.chat_threads:
    st.sidebar.info("No past research yet.")
else:
    for i, item in enumerate(reversed(st.session_state.chat_threads)):
        if st.sidebar.button(item["query"][:50], key=f"thread-{i}"):
            st.session_state.thread = item["thread"]
            st.session_state.query = item["query"]
            st.session_state.phase = "done"
            st.rerun()

# ── SECTION 1: HERO ──
st.title("🔬 Agentic Research Assistant")
st.caption("LangGraph · Groq · Tavily")
st.markdown("Ask a question. The agent searches the web, writes a sourced answer, and waits for **your approval** before finishing.")
st.markdown("`Your Query` → `Rewrite` → `Web Search` → `Synthesize` → `Critic` → `You Approve`")
st.divider()

# ── SECTION 2: INPUT ──
st.subheader("What do you want to research?")
query = st.text_input("Enter your topic", placeholder="e.g. Impact of AI on software engineering jobs")

if st.button("Run Research", disabled=st.session_state.phase != "input"):
    if query.strip():
        st.session_state.query = query
        st.session_state.phase = "running"
        st.rerun()

st.divider()

# ── SECTION 3: RUNNING ──
if st.session_state.phase == "running":
    with st.status("Running research agent...", expanded=True) as status:
        st.write("🔄 Rewriting query...")
        st.write("🌐 Searching the web...")
        st.write("🧠 Synthesizing answer...")
        st.write("🔍 Critic checking quality...")

        agent.invoke(
            {
                "query": st.session_state.query,
                "search_query": "",
                "web_results": "",
                "final_answer": "",
                "needs_retry": False,
                "retry_count": 0,
                "human_approved": False,
                "human_feedback": "",
            },
            config=st.session_state.thread,
        )

        status.update(label="✅ Answer ready for your review", state="complete", expanded=False)

    st.session_state.phase = "approval"
    st.rerun()

# ── SECTION 4: HUMAN APPROVAL ──
if st.session_state.phase == "approval":
    state = agent.get_state(st.session_state.thread).values

    st.subheader("Review the Answer")
    st.markdown(state["final_answer"])
    st.divider()

    feedback = st.text_input("Type 'ok' to approve, or give feedback to improve", key="feedback")

    if st.button("Submit"):
        if feedback.strip():
            agent.invoke({"resume": feedback}, config=st.session_state.thread)

            updated = agent.get_state(st.session_state.thread).values

            if updated.get("human_approved"):
                st.session_state.phase = "done"
            else:
                st.session_state.phase = "running"

            st.rerun()

# ── SECTION 5: FINAL ANSWER ──
if st.session_state.phase == "done":
    state = agent.get_state(st.session_state.thread).values

    st.success("✅ Research complete!")
    st.subheader("Final Approved Answer")
    st.markdown(state["final_answer"])
    st.divider()

    # save to history if not already saved
    existing = [t["thread"] for t in st.session_state.chat_threads]
    if st.session_state.thread not in existing:
        st.session_state.chat_threads.append({
            "query": st.session_state.query,
            "thread": st.session_state.thread,
        })

    if st.button("Start New Research"):
        st.session_state.thread = new_thread()
        st.session_state.query = ""
        st.session_state.phase = "input"
        st.rerun()