def ask_question(prompt, correct_answers, lives, points):
    answer = input(prompt).strip().upper()
    if answer in correct_answers:
        print("Correct!\n")
        points += 1
    else:
        lives -= 1
        print("Incorrect. You lost 1 life.")
        print(f"Lives left: {lives}\n")
    return lives, points


def save_score(name, age, points, total_questions):
    score = (points / total_questions) * 100
    with open("scores.txt", "a") as file:
        file.write(f"{name},{age},{points}/{total_questions},{score:.0f}%\n")


print("🚘 Welcome to the BMW Quiz Game!")

name = input("What's your name? ").capitalize()
age_input = input("How old are you? ")

if not age_input.isdigit():
    print("Please enter a valid number for age.")
    exit()

age = int(age_input)
print(f"Hi {name}, you are {age} years old.")

if age < 18:
    print("Sorry, you must be at least 18 to play!")
    exit()

wants_to_play = input("Do you want to play? (yes/no) ").strip().lower()
if wants_to_play != "yes":
    print("That's okay. Maybe next time!")
    exit()

print("\nGreat! Let's begin the quiz.")
lives = 5
points = 0
total_questions = 7
print(f"You start with {lives} lives.\n")

# Question 1
q1 = "1. Which of the following models does NOT belong to BMW?\nA. 1600\nB. Z8\nC. 2001C\n"
lives, points = ask_question(q1, {"C", "2001C"}, lives, points)
if lives == 0: exit("Game Over!")

# Question 2
q2 = "2. What is the horsepower of the BMW 740i model?\nA. 215\nB. 315\nC. 415\n"
lives, points = ask_question(q2, {"B", "315"}, lives, points)
if lives == 0: exit("Game Over!")

# Question 3
q3 = "3. Which luxury car brand was acquired by BMW in 1998?\nA. Jaguar\nB. Bentley\nC. Rolls-Royce\n"
lives, points = ask_question(q3, {"C", "ROLLS-ROYCE"}, lives, points)
if lives == 0: exit("Game Over!")

# Question 4
q4 = "4. BMW's headquarters is in which German city?\nA. Frankfurt\nB. Munich\nC. Stuttgart\n"
lives, points = ask_question(q4, {"B", "MUNICH"}, lives, points)
if lives == 0: exit("Game Over!")

# Question 5
q5 = "5. In which year was BMW founded?\nA. 1906\nB. 1916\nC. 1926\n"
lives, points = ask_question(q5, {"B", "1916"}, lives, points)
if lives == 0: exit("Game Over!")

# Question 6
q6 = "6. What does BMW stand for?\nA. Bavarian Motor Works\nB. Berlin Motor Works\nC. British Motor Works\n"
lives, points = ask_question(q6, {"A", "BAVARIAN MOTOR WORKS"}, lives, points)
if lives == 0: exit("Game Over!")

# Question 7
q7 = "7. What is BMW’s performance division called?\nA. AMG\nB. M Division\nC. RS\n"
lives, points = ask_question(q7, {"B", "M DIVISION"}, lives, points)
if lives == 0: exit("Game Over!")

# Final score
score_percent = (points / total_questions) * 100
print(f"Quiz Finished! You got {points} out of {total_questions}.")
print(f"Your score: {score_percent:.0f}%")

# Save to file
save_score(name, age, points, total_questions)
print("Your score has been saved to 'scores.txt'.")
