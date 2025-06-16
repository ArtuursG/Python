# 🏎️ BMW Quiz Game

This is a simple Python terminal quiz game about BMW. 
The player answers 7 multiple-choice questions and tries not to lose all 5 
lives before the end. Scores are saved to a file after each game session.

## 📂 What’s inside?

A single Python script:
- Asks for your name and age
- Checks if you’re old enough (18+)
- Lets you play a quiz about BMW models, history, and facts
- Tracks your lives and points
- Saves results in a `scores.txt` file

## 🧠 Sample Questions
- Which car model does **not** belong to BMW?
- What is the horsepower of the BMW 740i?
- What is BMW’s performance division called?

## ▶️ How to run it

Make sure you have Python installed.  
In terminal or Git Bash:

```
git clone https://github.com/ArtuursG/BMW-quiz.git
cd BMW-quiz
python bmw_quiz.py
```

---
## 💾 Output

Each result is saved in a text file scores.txt in the following format:
```
Name,Age,Correct/Total,Score%
```
Example: 
```
John,23,6/7,86%
```

---

## 📌 Notes
- The game is beginner-friendly and written in plain Python (no extra libraries).
- You start with 5 lives and lose one for each incorrect answer.
- Game ends if all lives are lost before completing the quiz.

---