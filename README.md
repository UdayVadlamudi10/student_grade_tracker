# Student Performance & Grade Tracker

An object-oriented Python CLI application designed to record, validate, and compute student academic metrics, including total marks, averages, and pass/fail statuses.

---

## Features

- **OOP Design:** Encapsulates student data and grading logic within a `Student` class.
- **Input Validation:** Restricts marks to integers strictly between `0` and `100`, prompting the user until a valid score is supplied.
- **Automated Grading:** Calculates cumulative scores, arithmetic averages, and pass/fail standing (minimum 40% passing threshold).
- **Formatted Reporting:** Outputs structured academic report summaries for batch students.

---

## Tech Stack

- **Language:** Python 3.14.7
- **Libraries:** Python Standard Library (no external dependencies required)
- **Version Control:** Git & GitHub

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/UdayVadlamudi10/week5-git-practice.git
   cd student-grade-tracker

2. **Verify Python Version:**
    python --version

3. **How to Run:**
    python main.py

4. **Example Output:**
    Students count: 1
Subjects count: 3
Enter student 1 name: Alice
Enter marks for subject 1: 85
Enter marks for subject 2: 120
Invalid: Mark must be between 0 and 100
Please enter the mark again.
Enter marks for subject 2: 78
Enter marks for subject 3: 92

--- Student Reports ---
Name: Alice
Marks: [85, 78, 92]
Total: 255
Average: 85.0
Result: Pass
-------------------------

## Limitations & Future Improvements

Current Limitations:
Data exists only in memory and resets once program execution terminates.
Scores are currently limited to integers rather than floating-point values.

Future Improvements:
Persist records using SQLite or export results to CSV/JSON files.
Add grade boundaries (A, B, C, D) alongside Pass/Fail.