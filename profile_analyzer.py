"""
Profile Analyzer Module
Processes user input and determines learning parameters.
"""

def analyze_profile(name: str, goal: str, level: str, hours: float, days: int) -> dict:
    """
    Analyze user profile and return structured learning parameters.

    Args:
        name: User's name
        goal: Learning goal/topic
        level: Skill level (beginner/intermediate/advanced)
        hours: Study hours per day
        days: Total days available

    Returns:
        dict: Structured profile with computed learning parameters
    """
    total_hours = hours * days

    pace_map = {
        "beginner": {"label": "Steady", "topics_per_hour": 0.7},
        "intermediate": {"label": "Moderate", "topics_per_hour": 1.0},
        "advanced": {"label": "Fast", "topics_per_hour": 1.3},
    }

    pace = pace_map.get(level, pace_map["beginner"])
    estimated_topics = int(total_hours * pace["topics_per_hour"])

    return {
        "name": name or "Learner",
        "goal": goal,
        "level": level,
        "hours": hours,
        "days": days,
        "total_hours": total_hours,
        "pace": pace["label"],
        "estimated_topics": estimated_topics,
        "difficulty_weight": {"beginner": 1, "intermediate": 1.5, "advanced": 2}.get(level, 1),
    }
