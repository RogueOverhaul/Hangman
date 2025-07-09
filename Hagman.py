import random as rnd
import re

def start_game():
    current_word = re.sub(r'\w', '_', word)
    tried_letters = []
    incorrect_tries = 0
    correct_letters = []
    while True:
        if incorrect_tries < 3:
            if word != current_word:
                print(current_word)
                print(f'Tried letters: {tried_letters}')
                print(f'You have {3 - incorrect_tries} attempts left')
                letter = input('Enter a letter: ')
                if letter in word:
                    print(f'Correct! {letter} is in the word.')
                    correct_letters.append(letter)
                else:
                    print(f'Sorry! {letter} is not in the word.')
                    incorrect_tries += 1
                for i in range(len(word)):
                    if letter == word[i]:
                        current_word = current_word[:i] + word[i] + current_word[i + 1:]
                tried_letters.append(letter)
            else:
                print(f'Congratulations! {current_word} is the hidden word! You won!')
                break
        else:
            print(f"Game Over! The word was: {word}")
            break

easy_words = ['bell',
                  'star',
                  'spider web',
                  'book',
                  'plant',
                  'snake',
                  'cherry',
                  'backpack',
                  'zoo',
                  'float',
                  'bird',
                  'carrot',
                  'broom',
                  'lamp',
                  'apple']
medium_words = ['gumball',
                    'rattle',
                    'jar',
                    'flood',
                    'helium',
                    'vegetable',
                    'rolly polly',
                    'lip',
                    'flashlight',
                    'sailboat',
                    'seed',
                    'newborn']
hard_words = ['driveway',
                  'water buffalo',
                  'neighborhood',
                  'ounce',
                  'boa constrictor',
                  'gold medal',
                  'deep',
                  'snore',
                  'stuffed animal',
                  'hail']
difficulty = ['1.-Easy', '2.-Medium', '3.-Hard']
while True:
    print("Hangman game")
    for i in difficulty:
        print(i)
    number = input("Enter your number:")
    if not number in ["1", "2", "3"]:
        print("Wrong difficulty!.")
        continue
    else:
        if number == "1":
            word = rnd.choice(easy_words)
            print("Level easy")
            start_game()
            break

        elif number == "2":
            word = rnd.choice(medium_words)
            print("Level medium")
            start_game()

        elif number == "3":
            word = rnd.choice(hard_words)
            print("Level hard")
            start_game()
            break
