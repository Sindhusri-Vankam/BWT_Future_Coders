"""
Progress Tracking Dashboard
Displays visual progress metrics using Streamlit + Matplotlib.
"""

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def show_progress_dashboard(plan: list, completed: dict, profile: dict):
    """
    Renders the full progress tracking dashboard.

    Args:
        plan: The generated learning plan
        completed: Dict mapping topic index -> bool (done/not done)
        profile: User profile dict
    """
    all_topics = [t for d in plan for t in d["topics"]]
    total = len(all_topics)
    done_count = sum(1 for v in completed.values() if v)
    progress_pct = round((done_count / total) * 100) if total else 0

    st.markdown(f"## 📈 Progress Dashboard — {profile.get('goal', 'Your Goal')}")

    # ── Top Metrics ──────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🎯 Overall Progress", f"{progress_pct}%")
    c2.metric("✅ Topics Done", f"{done_count}/{total}")
    c3.metric("📅 Days Planned", len(plan))
    days_complete = sum(
        1 for di, d in enumerate(plan)
        if all(completed.get(_topic_global_index(plan, di, ti), False) for ti in range(len(d["topics"])))
    )
    c4.metric("🏆 Days Complete", days_complete)

    st.divider()

    col_left, col_right = st.columns(2)

    # ── Donut Chart ───────────────────────────────────────
    with col_left:
        st.markdown("### Overall Completion")
        fig, ax = plt.subplots(figsize=(4, 4), facecolor="#0b0f1a")
        ax.set_facecolor("#0b0f1a")
        sizes = [done_count, total - done_count] if done_count < total else [total, 0.001]
        colors = ["#38bdf8", "#1e2a3a"]
        wedges, _ = ax.pie(sizes, colors=colors, startangle=90, wedgeprops=dict(width=0.45))
        ax.text(0, 0, f"{progress_pct}%", ha="center", va="center",
                fontsize=22, fontweight="bold", color="#e2e8f0")
        ax.text(0, -0.18, "Complete", ha="center", va="center",
                fontsize=10, color="#64748b")
        st.pyplot(fig)
        plt.close()

    # ── Day-wise Bar Chart ────────────────────────────────
    with col_right:
        st.markdown("### Day-wise Progress")
        day_labels = []
        day_pcts = []
        for di, day in enumerate(plan):
            day_done = sum(1 for ti in range(len(day["topics"])) if completed.get(_topic_global_index(plan, di, ti), False))
            pct = round((day_done / len(day["topics"])) * 100) if day["topics"] else 0
            day_labels.append(f"D{day['day']}")
            day_pcts.append(pct)

        fig2, ax2 = plt.subplots(figsize=(5, 4), facecolor="#0b0f1a")
        ax2.set_facecolor("#0b0f1a")
        bar_colors = ["#34d399" if p == 100 else "#38bdf8" if p > 0 else "#1e2a3a" for p in day_pcts]
        bars = ax2.bar(day_labels, day_pcts, color=bar_colors, width=0.6, edgecolor="none")
        ax2.set_ylim(0, 110)
        ax2.set_ylabel("% Complete", color="#64748b", fontsize=9)
        ax2.tick_params(colors="#64748b")
        ax2.spines["top"].set_visible(False)
        ax2.spines["right"].set_visible(False)
        for spine in ["left", "bottom"]:
            ax2.spines[spine].set_color("#1e2a3a")
        for bar, pct in zip(bars, day_pcts):
            if pct > 0:
                ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
                         f"{pct}%", ha="center", va="bottom", fontsize=7, color="#94a3b8")
        st.pyplot(fig2)
        plt.close()

    st.divider()

    # ── Topic Checklist ───────────────────────────────────
    st.markdown("### 📋 Topic Checklist")
    topic_idx = 0
    for day in plan:
        with st.expander(f"Day {day['day']}", expanded=False):
            for t in day["topics"]:
                done = completed.get(topic_idx, False)
                icon = "✅" if done else "⬜"
                status = "~~" if done else ""
                st.markdown(f"{icon} {status}{t['name']}{status} &nbsp;&nbsp; `{t['duration']}h`", unsafe_allow_html=True)
                topic_idx += 1

    # ── Completion message ────────────────────────────────
    if progress_pct == 100:
        st.success("🎉 **Congratulations! You've completed your entire learning plan!** You're amazing!")
    elif progress_pct >= 50:
        st.info(f"💪 You're over halfway there! Keep going — {total - done_count} topics left.")
    elif done_count > 0:
        st.info(f"🚀 Great start! {done_count} topics down, {total - done_count} to go.")


def _topic_global_index(plan: list, day_index: int, topic_index: int) -> int:
    """Helper: get the global flat index of a topic from its day + position."""
    idx = 0
    for di, day in enumerate(plan):
        for ti in range(len(day["topics"])):
            if di == day_index and ti == topic_index:
                return idx
            idx += 1
    return idx
