import random

coin = random.choice(["Heads", "Tails"])

print("🪙 Welcome to the Coin Tossing Game!")
print("Choose Heads or Tails.")

guess = input("Your choice: ").capitalize()

print("The coin landed on:", coin)

if guess == coin:
    print("🎉 Correct! You win!")
else:
    print("❌ Wrong! Better luck next time!")
    