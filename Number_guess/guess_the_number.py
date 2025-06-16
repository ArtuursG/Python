import random

print("Hi! What's your name?")
name = input("> ")

print(f"Nice to meet you, {name}! Let's play a game.")
print("I'm thinking of a number between 1 and 20. Try to guess it in less than 6 attempts.")

number = random.randint(1, 20)
guesses_taken = 0
max_guesses = 6

while guesses_taken < max_guesses:
    try:
        guess = int(input("Take a guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    guesses_taken += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"YAAAAYYY, good job {name}! You guessed the number in {guesses_taken} guesses!")
        break
else:
    print(f"Sorry, {name}. The number I was thinking of was {number}. Better luck next time!")
