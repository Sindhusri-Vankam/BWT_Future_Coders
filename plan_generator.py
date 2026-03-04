"""
Study Plan Generator
Creates a personalized day-wise learning schedule.
"""


def generate_plan(topics: list[dict], hours_per_day: float, total_days: int) -> list[dict]:
    """
    Generate a day-wise study plan from a list of topics.

    Args:
        topics: List of topic dicts (name, difficulty, duration)
        hours_per_day: Available study hours per day
        total_days: Total number of days in the plan

    Returns:
        List of day dicts, each with a list of topics and total hours
    """
    plan = []
    topic_queue = list(topics)
    day = 1

    while topic_queue and day <= total_days:
        day_topics = []
        remaining_hours = hours_per_day

        while topic_queue and remaining_hours > 0:
            topic = topic_queue[0]
            if topic["duration"] <= remaining_hours + 0.1:  # small tolerance
                day_topics.append(topic)
                remaining_hours -= topic["duration"]
                topic_queue.pop(0)
            else:
                break  # Not enough time left today for next topic

        if day_topics:
            plan.append({
                "day": day,
                "topics": day_topics,
                "total_hours": round(sum(t["duration"] for t in day_topics), 1),
            })

        day += 1

    return plan


def get_plan_summary(plan: list[dict]) -> dict:
    """
    Returns summary statistics for a generated plan.
    """
    all_topics = [t for d in plan for t in d["topics"]]
    return {
        "total_days": len(plan),
        "total_topics": len(all_topics),
        "total_hours": round(sum(t["duration"] for t in all_topics), 1),
        "difficulty_breakdown": {
            diff: len([t for t in all_topics if t.get("difficulty") == diff])
            for diff in set(t.get("difficulty", "Core") for t in all_topics)
        },
    }
