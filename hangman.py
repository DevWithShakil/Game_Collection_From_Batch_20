import random

def play_hangman():
    words = ["python", "developer", "terminal", "algorithm", "keyboard"]
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6

    print("--- Welcome to Hangman! ---")

    while attempts > 0:
        # Display current word state
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print("\nWord:", " ".join(display_word))
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        # Check win condition
        if "_" not in display_word:
            print(f"\n🎉 You won! The word was: {word}")
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong! '{guess}' is not in the word.")

    print(f"\n👻 Game over! The word was: {word}")

play_hangman()