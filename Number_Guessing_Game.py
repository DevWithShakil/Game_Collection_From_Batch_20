import random

number = random.randint(1, 10)

print("🎮 Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 10.")

guess = int(input("Guess the number: "))

if guess == number:
    print("🎉 Correct! You won!")
else:
    print("❌ Wrong!")
    print("The correct number was:", number)