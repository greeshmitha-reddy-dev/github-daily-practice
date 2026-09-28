# Day 7 - Python While Loop
# Number Guessing Game

secret_number = 7
guess = 0

print("----- Number Guessing Game -----")
print("Guess the number between 1 and 10")

while guess != secret_number:

    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Congratulations! You guessed the correct number.")