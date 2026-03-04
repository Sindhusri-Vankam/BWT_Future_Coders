from flask import Flask, render_template, request

app = Flask(__name__)

# Enhanced Diagnostic Quiz - Tests proficiency levels
questions = [
    # Arrays - Beginner
    {"question": "What is an array?", "answer": "contiguous memory", "topic": "arrays", "level": "beginner"},
    {"question": "What is the time complexity of accessing an element by index in an array?", "answer": "O(1)", "topic": "arrays", "level": "beginner"},
    # Arrays - Intermediate
    {"question": "What is the time complexity of binary search?", "answer": "O(log n)", "topic": "arrays", "level": "intermediate"},
    {"question": "Which data structure uses LIFO?", "answer": "Stack", "topic": "arrays", "level": "intermediate"},
    # Arrays - Advanced
    {"question": "Explain the difference between an array and a linked list in terms of memory allocation.", "answer": "contiguous vs scattered", "topic": "arrays", "level": "advanced"},
    
    # Recursion - Beginner
    {"question": "What is recursion?", "answer": "function calling itself", "topic": "recursion", "level": "beginner"},
    {"question": "What is a base case in recursion?", "answer": "stopping condition", "topic": "recursion", "level": "beginner"},
    # Recursion - Intermediate
    {"question": "What is tail recursion?", "answer": "recursive call is last operation", "topic": "recursion", "level": "intermediate"},
    # Recursion - Advanced
    {"question": "What is memoization and why is it used in recursion?", "answer": "caching results to avoid recomputation", "topic": "recursion", "level": "advanced"},
    
    # Sorting - Beginner
    {"question": "What does sorting mean?", "answer": "arranging in order", "topic": "sorting", "level": "beginner"},
    # Sorting - Intermediate
    {"question": "Best case time complexity of quicksort?", "answer": "O(n log n)", "topic": "sorting", "level": "intermediate"},
    {"question": "Which sorting algorithm is stable?", "answer": "Merge sort", "topic": "sorting", "level": "intermediate"},
    # Sorting - Advanced
    {"question": "Why is quicksort preferred over merge sort in practice despite same average complexity?", "answer": "better cache locality, less memory", "topic": "sorting", "level": "advanced"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz", methods=["POST"])
def quiz():
    daily_time = request.form["daily_time"]
    days = request.form["days"]
    stress = request.form["stress"]
    return render_template("quiz.html", questions=questions,
                           daily_time=daily_time,
                           days=days,
                           stress=stress)

@app.route("/result", methods=["POST"])
def result():
    daily_time = int(request.form["daily_time"])
    days = int(request.form["days"])
    stress = int(request.form["stress"])

    # Calculate proficiency levels (0-2 for beginner, 2-1 for intermediate, 1-0 for advanced)
    proficiency = {"arrays": "unknown", "recursion": "unknown", "sorting": "unknown"}
    scores_by_level = {"arrays": {}, "recursion": {}, "sorting": {}}
    
    for i, q in enumerate(questions):
        topic = q["topic"]
        level = q["level"]
        user_answer = request.form.get(f"q{i}")
        
        if topic not in scores_by_level:
            scores_by_level[topic] = {}
        if level not in scores_by_level[topic]:
            scores_by_level[topic][level] = {"correct": 0, "total": 0}
        
        scores_by_level[topic][level]["total"] += 1
        
        if user_answer and user_answer.strip().lower() == q["answer"].lower():
            scores_by_level[topic][level]["correct"] += 1

    # Determine proficiency level for each topic
    proficiency_levels = {}
    for topic in proficiency:
        beginner_score = scores_by_level[topic].get("beginner", {}).get("correct", 0) / max(1, scores_by_level[topic].get("beginner", {}).get("total", 1))
        intermediate_score = scores_by_level[topic].get("intermediate", {}).get("correct", 0) / max(1, scores_by_level[topic].get("intermediate", {}).get("total", 1))
        advanced_score = scores_by_level[topic].get("advanced", {}).get("correct", 0) / max(1, scores_by_level[topic].get("advanced", {}).get("total", 1))
        
        if beginner_score < 0.5:
            proficiency_levels[topic] = "beginner"
        elif intermediate_score < 0.5:
            proficiency_levels[topic] = "intermediate"
        else:
            proficiency_levels[topic] = "advanced"

    # Generate smart, selective content (100% offline, no API)
    plan = generate_smart_content(proficiency_levels, daily_time, days, stress)

    return render_template("result.html",
                           proficiency=proficiency_levels,
                           plan=plan,
                           daily_time=daily_time,
                           days=days,
                           stress=stress)

def generate_smart_content(proficiency, daily_time, days, stress):
    """Generate SELECTIVE, targeted content WITHOUT API calls - using local templates."""
    
    weak_topics = [t for t, p in proficiency.items() if p == "beginner"]
    strong_topics = [t for t, p in proficiency.items() if p == "advanced"]
    
    # Content templates - organized by topic and proficiency level
    content_library = {
        "arrays": {
            "beginner": {
                "title": "Arrays - Fundamentals",
                "content": """
1️⃣ WHY ARRAYS MATTER
Arrays are the foundation of data structures. Every competitive programmer must master them.

2️⃣ CORE CONCEPTS
• Array: Contiguous block of memory storing elements of the same type
• Indexing: Access elements in O(1) time using index (e.g., arr[0])
• Time Complexity: Access O(1), Search O(n), Insert O(n), Delete O(n)
• Memory: Arrays are fixed-size; use dynamic arrays (lists) for flexibility

3️⃣ QUICK EXAMPLE
```
arr = [10, 20, 30, 40]
print(arr[0])  # Output: 10 (O(1) access)
```

4️⃣ PRACTICE PROBLEM
Q: Find the maximum element in an array
A: Loop through and track the max
Time: O(n), Space: O(1)

5️⃣ KEY TAKEAWAY
Master array access patterns. Most problems start with arrays!
                """
            },
            "intermediate": {
                "title": "Arrays - Searching & Sorting",
                "content": """
1️⃣ BINARY SEARCH (Most Important!)
Only works on SORTED arrays. Reduces search from O(n) to O(log n).

Key Idea: Start at middle, eliminate half with each step
```
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found
```

2️⃣ TWO POINTER TECHNIQUE
Used for: sorted arrays, finding pairs, removing duplicates

Example: Find if two elements sum to target
```
def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

3️⃣ SLIDING WINDOW
Find subarray matching condition (length, sum, etc.)

Example: Max sum of k consecutive elements
```
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

4️⃣ PRACTICE
• LeetCode #1: Two Sum
• LeetCode #33: Search in Rotated Sorted Array
• LeetCode #209: Minimum Size Subarray Sum
                """
            },
            "advanced": {
                "title": "Arrays - Advanced Patterns",
                "content": """
1️⃣ PREFIX SUM / CUMULATIVE SUM
Precompute cumulative sums to answer range queries in O(1)

```
def range_sum(arr, left, right):
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)
    return prefix[right+1] - prefix[left]
```

2️⃣ MONOTONIC STACK
Solve next greater/smaller element problems in O(n)

Example: Next Greater Element
```
def next_greater(arr):
    result = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result
```

3️⃣ FREQUENCY ARRAYS / COUNTING SORT
O(n) sorting when values have bounded range

4️⃣ BIT MANIPULATION
XOR for finding unpaired elements, bit operations for optimization

5️⃣ INTERVIEW PROBLEMS
• Maximum Subarray (Kadane's Algorithm)
• Trapping Rain Water
• Product of Array Except Self
• Merge Sorted Arrays
• Median of Two Sorted Arrays
                """
            }
        },
        "recursion": {
            "beginner": {
                "title": "Recursion - Essentials",
                "content": """
1️⃣ WHAT IS RECURSION?
A function calling itself to solve smaller versions of the same problem.

2️⃣ TWO CRITICAL COMPONENTS
✓ BASE CASE: When to STOP recursing (prevent infinite loop)
✓ RECURSIVE CASE: Call yourself with a simpler input

3️⃣ SIMPLE EXAMPLE: Factorial
```
def factorial(n):
    if n == 1:           # BASE CASE
        return 1
    return n * factorial(n-1)  # RECURSIVE CASE
    
factorial(5) = 5 * factorial(4)
             = 5 * 4 * factorial(3)
             = 5 * 4 * 3 * 2 * 1 = 120
```

4️⃣ ANOTHER EXAMPLE: Sum of Array
```
def sum_array(arr):
    if len(arr) == 0:          # BASE CASE
        return 0
    return arr[0] + sum_array(arr[1:])  # RECURSIVE CASE
```

5️⃣ COMMON MISTAKES
❌ No base case → Stack overflow
❌ Wrong base case → Infinite recursion
❌ Not making progress toward base case → Never terminates

6️⃣ PRACTICE
Write recursive functions for: Fibonacci, Reverse String, Count Down
                """
            },
            "intermediate": {
                "title": "Recursion - Trees & Backtracking",
                "content": """
1️⃣ TREE RECURSION
Problems where each call makes multiple recursive calls

Example: Fibonacci
```
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)  # TWO recursive calls!
```
Issue: fib(5) recalculates fib(3) multiple times → BAD
Solution: Use memoization!

2️⃣ MEMOIZATION (Caching Results)
```
def fib(n, memo={}):
    if n in memo:
        return memo[n]     # Return cached result
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

3️⃣ BACKTRACKING PATTERN
Try all possibilities, undo choices that don't work

```
def backtrack(candidates):
    result = []
    
    def solve(path, remaining):
        if is_solution(path):
            result.append(path)
            return
        
        for choice in candidates:
            path.append(choice)
            if is_valid(path):
                solve(path, remaining)
            path.pop()  # UNDO choice
    
    solve([], candidates)
    return result
```

4️⃣ CLASSIC PROBLEMS
• Permutations: Generate all orderings
• Combinations: Select k items from n
• N-Queens: Place queens without attacking
• Sudoku Solver: Fill grid with constraints
• Word Search: Path through grid

5️⃣ PRACTICE
LeetCode: Permutations, Combinations, Word Search, N-Queens
                """
            },
            "advanced": {
                "title": "Recursion - Divide & Conquer",
                "content": """
1️⃣ DIVIDE & CONQUER STRATEGY
1. DIVIDE: Break problem into independent subproblems
2. CONQUER: Solve subproblems recursively
3. COMBINE: Merge results

2️⃣ MERGE SORT (Classic Example)
```
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])      # Divide & Conquer left
    right = merge_sort(arr[mid:])     # Divide & Conquer right
    
    return merge(left, right)         # Combine
```

3️⃣ QUICK SORT
Choose pivot, partition, recursively sort left and right

4️⃣ BINARY SEARCH (Recursive)
```
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, right)
    else:
        return binary_search(arr, target, left, mid-1)
```

5️⃣ MASTER THEOREM (Analyze Complexity)
T(n) = aT(n/b) + f(n)
• If f(n) = O(n^c) where c < log_b(a) → T(n) = O(n^log_b(a))
• Use this to analyze divide-and-conquer algorithms

6️⃣ INTERVIEW PROBLEMS
• Merge K Sorted Lists
• Majority Element
• Closest Pair of Points
• Inversion Count in Array
                """
            }
        },
        "sorting": {
            "beginner": {
                "title": "Sorting - Fundamentals",
                "content": """
1️⃣ WHY SORTING MATTERS
Sorting is the foundation for searching, interviews, and optimization

2️⃣ BUBBLE SORT (Easiest, but SLOW)
Repeatedly swap adjacent elements if they're in wrong order
```
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```
Time: O(n²) - TOO SLOW for interviews!

3️⃣ SELECTION SORT
Find minimum each time, move it to front
```
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```
Time: O(n²) - Also SLOW

4️⃣ INSERTION SORT
Like sorting playing cards. Good for small arrays!
```
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
```
Time: O(n²), but O(n) if nearly sorted!

5️⃣ RULE OF THUMB
These O(n²) sorts are TOO SLOW. Use only for learning!
For interviews: Use O(n log n) algorithms!
                """
            },
            "intermediate": {
                "title": "Sorting - Fast Algorithms",
                "content": """
1️⃣ MERGE SORT (Guaranteed O(n log n))
Divide array in half, sort each half, merge them

```
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```
Time: O(n log n) guaranteed
Space: O(n) - uses extra memory
Stable: Yes (preserves order of equal elements)

2️⃣ QUICK SORT (Fastest in practice)
Pick pivot, partition, recursively sort left/right

```
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
```
Time: O(n log n) average, O(n²) worst case
Space: O(log n) due to recursion
Stable: No (depending on implementation)

3️⃣ WHEN TO USE WHICH?
• Merge Sort: When you NEED O(n log n) guaranteed and stability
• Quick Sort: Fastest in practice, interactive systems
• Heap Sort: External sorting when memory is limited
• Radix Sort: Only integers, O(nk) where k=digits

4️⃣ PRACTICE PROBLEMS
LeetCode: Sort an Array, Merge Sorted Array
                """
            },
            "advanced": {
                "title": "Sorting - Advanced & Custom",
                "content": """
1️⃣ HEAP SORT (Space-Efficient O(n log n))
Build max heap, repeatedly extract max

```
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left, right = 2*i + 1, 2*i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
```

2️⃣ RADIX SORT (For Integers)
Sort by individual digits. O(nk) where k=digits
```
def radix_sort(arr):
    if not arr:
        return arr
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr
```

3️⃣ CUSTOM SORTING (Important for Interviews!)
Use custom comparators for sorting objects

```
# Sort by multiple criteria
people = [("Alice", 25), ("Bob", 20), ("Charlie", 25)]
sorted_people = sorted(people, key=lambda x: (x[1], x[0]))
```

4️⃣ STABILITY & COMPARISONS
Stable sorts preserve order of equal elements
Merge Sort & Insertion Sort are stable
Quick Sort & Heap Sort are not stable

5️⃣ INTERVIEW QUESTIONS
• Sort colors (3-way partition)
• Sort linked list
• Merge k sorted lists
• Top K frequent elements (MinHeap)
• Largest rectangle in histogram
                """
            }
        }
    }
    
    # Study time allocation
    total_hours = daily_time * days
    weak_topic_count = len(weak_topics) if weak_topics else 1
    hours_per_topic = total_hours / weak_topic_count if weak_topics else total_hours
    
    # Build personalized plan based on proficiency
    plan_sections = []
    
    # Motivation
    stress_msg = {
        1: "You've got this! Stress level low - time to dig deep! 💪",
        10: "Breathe! We'll focus only on what you truly need. 🎯"
    }
    
    motivation = stress_msg.get(min(stress, 10), f"You can do it! Let's maximize your {daily_time}h/day. ⏰")
    plan_sections.append(f"🎯 PERSONALIZED PLAN\n\n{motivation}\n")
    
    # Content for weak topics only
    if weak_topics:
        plan_sections.append(f"\n📚 YOUR FOCUS AREAS (Master These)\n{'='*50}\n")
        
        for topic in weak_topics:
            if topic in content_library:
                topic_content = content_library[topic]["beginner"]
                plan_sections.append(f"\n{topic_content['title'].upper()}")
                plan_sections.append(topic_content['content'])
    else:
        plan_sections.append("\n✅ YOU'RE SOLID! You know the basics well.\nFocus on: Solving real interview problems, optimizing solutions, and building speed.\n")
    
    # Study schedule
    plan_sections.append(f"\n\n📅 YOUR {days}-DAY STUDY SCHEDULE\n{'='*50}\n")
    
    if weak_topics:
        hours_per_day_per_topic = daily_time / weak_topic_count
        current_day = 1
        for topic in weak_topics:
            days_for_topic = max(1, int(hours_per_topic / daily_time))
            plan_sections.append(f"\nDAYS {current_day}-{current_day + days_for_topic - 1}: {topic.upper()}")
            plan_sections.append(f"• Study time: {min(daily_time, hours_per_topic):.1f}h per day")
            plan_sections.append(f"• Focus: Understand core concepts, do practice problems")
            plan_sections.append(f"• Stress adjustment: {'Light pace' if stress > 7 else 'Medium pace' if stress > 4 else 'Aggressive pace'}")
            current_day += days_for_topic
    else:
        plan_sections.append("• Days 1-7: Practice interview-level problems from your strong areas")
        plan_sections.append("• Focus: Speed and optimization, not fundamentals")
    
    # Tips
    plan_sections.append(f"\n\n💡 PRO TIPS\n{'='*50}")
    if stress > 7:
        plan_sections.append("• High stress detected: Take breaks! 30min study + 5min break = better learning")
    plan_sections.append("• Don't skip practice problems - that's where learning happens")
    plan_sections.append("• If a concept is unclear, revisit the example multiple times")
    plan_sections.append("• Time is limited: Focus ONLY on weak topics, skip what you know")
    
    return {
        "weak_topics": weak_topics,
        "strong_topics": strong_topics,
        "plan": "\n".join(plan_sections)
    }

if __name__ == "__main__":
    app.run(debug=True)