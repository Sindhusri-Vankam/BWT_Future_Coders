import streamlit as st
from src.profile_analyzer import analyze_profile
from src.topic_engine import get_topics
from src.plan_generator import generate_plan
from src.progress_tracker import show_progress_dashboard

st.set_page_config(
    page_title="Overwhelmed Learner AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-title { font-size: 2.5rem; font-weight: 800; color: #38bdf8; }
    .subtitle { color: #94a3b8; font-size: 1.1rem; }
    .stat-card { background: #1e293b; padding: 20px; border-radius: 12px; text-align: center; }
    .topic-done { color: #34d399; }
    .topic-pending { color: #e2e8f0; }
</style>
""", unsafe_allow_html=True)

# Session state init
if "plan" not in st.session_state:
    st.session_state.plan = None
if "completed" not in st.session_state:
    st.session_state.completed = {}
if "step" not in st.session_state:
    st.session_state.step = "setup"

# ── Sidebar ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🧠 Overwhelmed Learner")
    st.markdown("*AI Productivity System*")
    st.divider()

    st.markdown("### 👤 Your Profile")
    name = st.text_input("Your Name", placeholder="e.g. Arjun")

    st.markdown("### 🎯 Learning Goal")
    goal = st.selectbox("Select Topic", [
        "Python Programming",
        "Machine Learning",
        "Web Development",
        "Data Science",
        "Custom Topic"
    ])

    if goal == "Custom Topic":
        custom_goal = st.text_input("Enter your topic", placeholder="e.g. Blockchain, Finance...")
        goal_label = custom_goal or "Custom Topic"
    else:
        goal_label = goal

    st.markdown("### ⚙️ Preferences")
    level = st.selectbox("Skill Level", ["Beginner", "Intermediate", "Advanced"])
    hours = st.slider("Hours per Day", 1.0, 6.0, 2.0, 0.5)
    days = st.selectbox("Deadline (days)", [7, 10, 14, 21, 30, 45, 60], index=2)

    st.divider()
    if st.button("🎯 Generate My Plan", use_container_width=True, type="primary"):
        profile = analyze_profile(name, goal_label, level.lower(), hours, days)
        topics = get_topics(goal, level.lower())
        st.session_state.plan = generate_plan(topics, hours, days)
        st.session_state.completed = {i: False for i in range(sum(len(d["topics"]) for d in st.session_state.plan))}
        st.session_state.profile = profile
        st.session_state.step = "plan"
        st.rerun()

    if st.session_state.plan:
        st.divider()
        nav = st.radio("Navigate", ["📅 Learning Plan", "📈 Progress Dashboard"], label_visibility="collapsed")
        if nav == "📅 Learning Plan":
            st.session_state.step = "plan"
        else:
            st.session_state.step = "progress"

# ── Main Content ──────────────────────────────────────────
if st.session_state.step == "setup":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="main-title">🧠 Overwhelmed Learner</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Your AI-powered personalized learning system</div>', unsafe_allow_html=True)
        st.markdown("")

        st.info("👈 Fill in your profile and click **Generate My Plan** to get started!")

        st.markdown("### 🚀 What this system does")
        cols = st.columns(3)
        features = [
            ("🎯", "Goal-Based Plans", "Breaks your topic into structured subtopics"),
            ("⏳", "Time-Aware", "Allocates daily study slots based on your schedule"),
            ("📈", "Progress Tracking", "Visual dashboard to track your learning journey"),
        ]
        for col, (icon, title, desc) in zip(cols, features):
            with col:
                st.markdown(f"**{icon} {title}**")
                st.caption(desc)

        st.markdown("### 📚 Supported Topics")
        st.markdown("""
        | Topic | Levels |
        |-------|--------|
        | Python Programming | Beginner → Advanced |
        | Machine Learning | Beginner → Advanced |
        | Web Development | Beginner → Advanced |
        | Data Science | Beginner → Advanced |
        | Custom Topic | All Levels |
        """)

elif st.session_state.step == "plan" and st.session_state.plan:
    profile = st.session_state.profile
    plan = st.session_state.plan

    st.markdown(f"## 📅 Learning Plan — {profile['goal']}")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Skill Level", profile["level"].capitalize())
    c2.metric("Hours/Day", f"{profile['hours']}h")
    c3.metric("Total Days", profile["days"])
    total_topics = sum(len(d["topics"]) for d in plan)
    c4.metric("Total Topics", total_topics)

    st.divider()
    topic_idx = 0
    for day in plan:
        with st.expander(f"📆 Day {day['day']} — {len(day['topics'])} topics · {day['total_hours']}h", expanded=day["day"] <= 3):
            for t in day["topics"]:
                key = f"topic_{topic_idx}"
                col1, col2 = st.columns([5, 1])
                with col1:
                    done = st.checkbox(t["name"], key=key, value=st.session_state.completed.get(topic_idx, False))
                    st.session_state.completed[topic_idx] = done
                with col2:
                    st.caption(f"⏱ {t['duration']}h")
                topic_idx += 1

elif st.session_state.step == "progress" and st.session_state.plan:
    show_progress_dashboard(st.session_state.plan, st.session_state.completed, st.session_state.profile)

else:
    st.warning("No plan generated yet. Fill in your profile in the sidebar and click Generate!")
