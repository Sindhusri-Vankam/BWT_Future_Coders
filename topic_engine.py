"""
Topic Breakdown Engine
Splits learning goals into structured, level-appropriate subtopics.
"""

TOPIC_MAP = {
    "Python Programming": {
        "beginner": [
            "Python Syntax & Variables", "Data Types & Operators",
            "Control Flow (if/else/loops)", "Functions & Scope",
            "Lists, Tuples & Dictionaries", "File Handling Basics",
            "Basic OOP Concepts",
        ],
        "intermediate": [
            "Advanced OOP & Inheritance", "Iterators & Generators",
            "Decorators & Context Managers", "Error & Exception Handling",
            "Modules, Packages & pip", "List Comprehensions & Lambda",
            "Regular Expressions",
        ],
        "advanced": [
            "Metaclasses & Descriptors", "Concurrency: Threads & Async",
            "C Extensions & Cython", "Memory Management & Profiling",
            "Design Patterns in Python", "Testing, TDD & pytest",
            "Performance Optimization",
        ],
    },
    "Machine Learning": {
        "beginner": [
            "Math Foundations (Linear Algebra)", "Statistics & Probability",
            "Python for ML (NumPy & Pandas)", "What is ML? Types & Use Cases",
            "Linear Regression", "Logistic Regression",
            "Model Evaluation Basics",
        ],
        "intermediate": [
            "Decision Trees & Random Forests", "SVM & Naive Bayes",
            "Feature Engineering & Selection", "Cross Validation Techniques",
            "Neural Network Basics", "Scikit-learn Pipelines",
            "Intro to Deep Learning",
        ],
        "advanced": [
            "CNNs & Image Classification", "RNNs & Sequence Models",
            "Transformers & Attention Mechanism", "Reinforcement Learning Basics",
            "GANs & Generative Models", "Model Deployment & Serving",
            "MLOps & Monitoring",
        ],
    },
    "Web Development": {
        "beginner": [
            "HTML5 Fundamentals", "CSS Basics & Selectors",
            "CSS Flexbox & Grid", "JavaScript Basics",
            "DOM Manipulation", "Forms & Validation",
            "Responsive Design Principles",
        ],
        "intermediate": [
            "ES6+ Modern JavaScript", "Fetch API & Async/Await",
            "React Fundamentals", "State Management & Props",
            "React Hooks (useState, useEffect)", "REST API Integration",
            "Version Control with Git",
        ],
        "advanced": [
            "Next.js & Server-Side Rendering", "TypeScript Essentials",
            "Testing with Jest & Cypress", "Web Performance Optimization",
            "GraphQL APIs", "CI/CD Pipelines", "System Design for Web",
        ],
    },
    "Data Science": {
        "beginner": [
            "Intro to Data Science Workflow", "Python Basics for DS",
            "NumPy Essentials", "Pandas DataFrames & Operations",
            "Data Cleaning & Preprocessing", "Exploratory Data Analysis",
            "Basic Visualization with Matplotlib",
        ],
        "intermediate": [
            "Advanced Visualization (Seaborn/Plotly)", "Statistical Analysis",
            "Hypothesis Testing", "SQL for Data Science",
            "Feature Engineering", "Intro to Machine Learning",
            "Data Storytelling",
        ],
        "advanced": [
            "Big Data & Apache Spark", "Time Series Analysis & Forecasting",
            "NLP Fundamentals", "A/B Testing & Experimentation",
            "Causal Inference", "Production Data Pipelines",
            "Deep Learning for Data Science",
        ],
    },
}

DEFAULT_TOPICS = {
    "beginner": [
        "Topic Foundations & Overview", "Core Concepts Part 1",
        "Core Concepts Part 2", "Basic Terminology",
        "Simple Applications", "Hands-on Practice 1",
        "Foundation Review & Assessment",
    ],
    "intermediate": [
        "Intermediate Concepts Overview", "Applied Techniques",
        "Problem Solving Methods", "Tools & Frameworks",
        "Real-world Mini Project", "Best Practices",
        "Intermediate Review",
    ],
    "advanced": [
        "Advanced Theory & Principles", "Complex Problem Sets",
        "Research & Innovation Approaches", "Performance Tuning",
        "Expert-Level Techniques", "Case Studies",
        "Advanced Capstone Review",
    ],
}


def get_topics(goal: str, level: str) -> list[dict]:
    """
    Get structured topics for a given goal and level.

    Args:
        goal: Learning goal (e.g., 'Python Programming')
        level: Skill level (beginner/intermediate/advanced)

    Returns:
        List of topic dicts with name and difficulty tag
    """
    topic_list = TOPIC_MAP.get(goal, {}).get(level) or DEFAULT_TOPICS.get(level, DEFAULT_TOPICS["beginner"])

    difficulty_tags = {
        "beginner": ["Foundation", "Foundation", "Foundation", "Core", "Core", "Core", "Review"],
        "intermediate": ["Core", "Applied", "Applied", "Practical", "Practical", "Best Practice", "Review"],
        "advanced": ["Advanced", "Advanced", "Expert", "Expert", "Expert", "Expert", "Capstone"],
    }
    tags = difficulty_tags.get(level, difficulty_tags["beginner"])

    return [
        {"name": name, "difficulty": tags[i] if i < len(tags) else "Core", "duration": 1.0 if i < 3 else 1.5}
        for i, name in enumerate(topic_list)
    ]
