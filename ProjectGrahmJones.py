# Hangman game !

import random


from ISProject.Hangman_with_GUI_and_Difficulties.EasyWords import easy_list
from ISProject.Hangman_with_GUI_and_Difficulties.NormalWords import normal_list
from ISProject.Hangman_with_GUI_and_Difficulties.HardWords import hard_list


# imports all of the words fro m each list ^

def get_difficulty_word():  # pick's the difficultly
    while True:
        mode_ui = input('What Difficulty Would You Like To Play?\n(E)asy, (N)ormal {recommended}, or (H)ard: ')
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
    guess_lett = []
    guess_words = []
    tries = 6

    print('Now, it is time to play the game!')
    print(hang_man(tries))  # turn this into the GUI at some point
    print(word_complete)
    print('\n')
    print('The word is', len(word_complete), ' letters long! \n Good luck! \n')

    while not guess and tries > 0:  # loop for UI letters and words
        guess_ui = input('Guess a letter, or the entire word if you know it: ').upper()

        if len(guess_ui) == 1 and guess_ui.isalpha():  # guessing letters

            if guess in guess_lett:  # repeat letter
                print("Sorry! You  have already guessed that letter: ", guess_ui)

            elif guess_ui not in word:  # wrong letter
                print('Sorry!', guess_ui, "is not in the word.")

                if tries >= 1:  # tries to ask the user to please try again, unless there are no more tries left
                    print('Please, try another Letter!')

                else:
                    pass

                tries -= 1

                guess_lett.append(guess_ui)

            else:
                print("Great job!", guess_ui, "is in the word!")

                guess_lett.append(guess_ui)
                word_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter == guess_ui]  # wtf does this do

                for index in indices:
                    word_list[index] = guess_ui
                word_complete = "".join(word_list)

                if "_" not in word_complete:
                    guess = True

        elif len(guess_ui) == len(word) and guess_ui.isalpha():  # for guessing words
            if guess_ui in guess_words:
                print("You already guessed the word", guess_ui)
            elif guess_ui != word:
                print(guess_ui, "is not the word.")
                tries -= 1
                guess_words.append(guess_ui)
            else:
                guess = True
                word_complete = word

        else:
            print('Not a valid input.')

        print(hang_man(tries))
        print(word_complete)
        print("\n")

    if guess:
        print("Congratulations, you have guessed the word! You win!")

    else:
        print("Sorry, but you ran out of tries :( \nThe word was " + word + ". Please, try again later!")


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
    word = get_difficulty_word()
    game(word)

    while input("Would you like to play Again? (Y/N) ").upper() == "Y":
        word = get_difficulty_word()
        game(word)


if __name__ == "__main__":
    main()
