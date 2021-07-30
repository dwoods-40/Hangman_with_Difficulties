# Hangman game !

import random

# importing word files
from Easy_Words import easy_list
from Normal_Words import normal_list
from Hard_Words import hard_list


# imports all of the words fro m each list ^

def get_difficulty():  # pick's the difficultly
    while True:
        mode_ui = input('What difficulty would you like to play?\n(E)asy, (N)ormal, or (H)ard: ')
        #  put function in each statement below so the correct difficulty gets put on word variable
        if mode_ui.lower() == 'e':  # play easy use another function if needed
            word = random.choice(easy_list)
            return word.upper()

        elif mode_ui.lower() == 'n':  # play normal
            word = random.choice(normal_list)
            return word.upper()

        elif mode_ui.lower() == 'h':  # play hard
            word = random.choice(hard_list)
            return word.upper()

        else:
            print('Invalid input, try again.')


def game(word):  # MAIN game
    word_complete = '_' * len(word)
    guess = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Lets play!')
    print(hang_man(tries))
    print(word_complete)
    print('\n')
    print('The word is', len(word_complete), ' letters long! \n Good luck! \n')

    while not guess and tries > 0:  # loop for UI letters and words
        guess_ui = input('Please guess a letter, or the entire word if you know it: ').upper()

        if len(guess_ui) == 1 and guess_ui.isalpha():  # guessing letters

            if guess_ui in guessed_letters:  # repeat letter
                print("Sorry! You  have already guessed that letter: ", guess_ui)

            elif guess_ui not in word:  # wrong letter
                print('Sorry!', guess_ui, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess_ui)
            else:
                print("Great job!", guess_ui, "is in the word!")
                guessed_letters.append(guess_ui)
                word_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter == guess_ui]

                for index in indices:
                    word_list[index] = guess_ui
                word_complete = "".join(word_list)

                if "_" not in word_complete:
                    guess = True

        elif len(guess_ui) == len(word) and guess_ui.isalpha():  # for guessing words
            if guess_ui in guessed_words:
                print("You already guessed the word", guess_ui)
            elif guess_ui != word:
                print(guess_ui, "is not the word.")
                tries -= 1
                guessed_words.append(guess_ui)
            else:
                guess = True
                word_complete = word

        else:
            print('Not a valid input.')

        print(hang_man(tries))
        print(word_complete)
        print("\n")

    if guess:
        print("Congratulations, you guessed the word! You win!")

    else:
        print("Sorry, you're ran out of tries :( \nThe word was " + word + ". Try again!")


def hang_man(tries):  # taken straight from reference code
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def main():
    word = get_difficulty()
    game(word)

    while input("Would you like to play again? (Y/N) ").upper() == "Y":
        word = get_difficulty()
        game(word)


if __name__ == "__main__":
    main()
