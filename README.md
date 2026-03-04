# 🧠 Overwhelmed Learner — AI Productivity System

> **Build for Focus and Flow** — A personalized AI learning path generator that eliminates information overload and helps you learn smarter.

---

## 📌 Problem Statement

Students and professionals face an overwhelming amount of learning resources. Most platforms provide generic content without considering:

- Individual skill level
- Available time
- Specific goals
- Deadlines

This leads to **information overload**, **poor focus**, and **burnout**.

---

## ✅ Solution

The **Overwhelmed Learner AI System** is a personalized learning path generator that:

- Analyzes your profile (skill level, goal, time availability)
- Breaks large topics into structured subtopics
- Prioritizes content based on difficulty
- Generates a **customized daily learning schedule**
- Tracks progress visually on a dashboard

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 🎯 Goal-Based Plans | Choose from Python, ML, Web Dev, Data Science, or custom topics |
| 📊 Skill Customization | Beginner / Intermediate / Advanced levels |
| ⏳ Time-Aware Planning | Set hours/day and deadline |
| 📅 Daily Allocation | Topics split across days intelligently |
| 📈 Progress Dashboard | Visual charts and topic checklist |
| 🧠 Smart Topic Structure | Topics ordered from basic → advanced |

---

## 🏗️ Project Structure

```
overwhelmed-learner/
│
├── app.py                  # Main Streamlit app entry point
├── requirements.txt        # Python dependencies
├── README.md               # This file
│
└── src/
    ├── __init__.py
    ├── profile_analyzer.py  # Analyzes user profile & learning params
    ├── topic_engine.py      # Topic breakdown by goal & skill level
    ├── plan_generator.py    # Day-wise study plan generator
    └── progress_tracker.py  # Progress dashboard with charts
```

---

## 🖥️ System Architecture

```
User Input (Streamlit Sidebar)
        ↓
Profile Analyzer Module
        ↓
Topic Breakdown Engine
        ↓
Study Plan Generator
        ↓
Progress Tracking Dashboard
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/overwhelmed-learner.git
cd overwhelmed-learner
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

### 5. Open in browser
The app will open at `http://localhost:8501`

---

## 🧑‍💻 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Data Processing | Python, Pandas, NumPy |
| Visualization | Matplotlib |
| Language | Python 3.10+ |

---

## 📸 App Flow

1. Enter your **name**, **learning goal**, **skill level**, **hours/day**, and **deadline**
2. Click **Generate My Plan** — your personalized schedule is created
3. View **day-wise topics** in the Learning Plan tab
4. Track your progress in the **Progress Dashboard**
5. Check off topics as you complete them

---

## 🔮 Future Enhancements

- [ ] AI-based resource recommendation (YouTube/Coursera links)
- [ ] Adaptive rescheduling if user misses a day
- [ ] Chatbot for doubt clarification
- [ ] Export plan to PDF / Excel
- [ ] User authentication & cloud sync

---

## 📄 License

MIT License — feel free to use and modify.

---

## 🙌 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change.
