import random
from words import words
import string

def get_valid_word(words):
    # some words in words.py have some extra space and - in them
    word = random.choice(words) # randomly choose a word from list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    # print(word)
    
    return word.upper()

def hangman():
    word  = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # Getting user input
    while len(word_letters) > 0: 
        # letters used
        print('You have used these letters : ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word : ', ' '.join(word_list))

        user_letter = input('Guess a letter : ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that letter. Try again')

        else: 
            print('Invalid character. Please try again')

    # gets here when len(word_letters) == 0
    print()
hangman()