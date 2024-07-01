# import random

# hangman_words = ["python", "hangman", "computer", "programming", "developer", "coding", "challenge", "game", "openai"]

# def choose_word():
#     return random.choice(hangman_words)

# def display_word(word, guessed_letters):
#     display = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display += letter
#         else:
#             display += "_"
#     return display

# def hangman():
#     word = choose_word()
#     guessed_letters = []
#     attempts = 6

#     print("Welcome to Hangman!")
#     print("Try to guess the word.")

#     while attempts > 0:
#         print("\nAttempts left:", attempts)
#         display = display_word(word, guessed_letters)
#         print("Word:", display)

#         if "_" not in display:
#             print("Congratulations! You won!")
#             return

#         guess = input("Enter a letter: ").lower()
# f
#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input. Please enter a single letter.")
#             continue

#         if guess in guessed_letters:
#             print("You've already guessed that letter.")
#             continue

#         guessed_letters.append(guess)

#         if guess not in word:
#             attempts -= 1
#             print("Incorrect guess.")
#             if attempts == 0:
#                 print("You lost! The word was:", word)
#                 return

#     print("You lost! The word was:", word)

# if __name__ == "__main__":
#     hangman()

import random

hangman_words = ["python", "hangman", "computer", "programming", "developer", "coding", "challenge", "game", "openai"]

def choose_word():
    return random.choice(hangman_words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        display = display_word(word, guessed_letters)
        print("Word:", display)

        if "_" not in display:
            print("Congratulations! You won!")
            return

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():  # Validate input before processing
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess.")
            if attempts == 0:
                print("You lost! The word was:", word)
                return

    print("You lost! The word was:", word)

if __name__ == "__main__":
    hangman()
