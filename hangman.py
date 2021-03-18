import random
from wordslist import data
import string


def get_valid_word(word_list):
    word = random.choice(word_list)  # randomly chooses word from data list in wordlist
    while "-" in word or " " in word:
        word = random.choice(data)

    return word


def hangman():
    valid_word = get_valid_word(data).upper()
    word_letters = set(valid_word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # holds the letters that were guessed.

    lives = 6

    while lives > 0 and len(word_letters) > 0:
        # letters used
        print("You have ", lives, "and you have used:", " ".join(used_letters))
        # what current word is
        word_list = [letter if letter in used_letters else "-" for letter in valid_word]
        print("Current word: ", " ".join(word_list))
        # get user input
        user_letter = input("Guess the letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print("You have already used that letter")

        else:
            print("Invalid Character, please try again.")
    if lives == 0:
        print("Sorry try again, the word was ", valid_word)
    else:
        print("You've guessed the word!")


hangman()