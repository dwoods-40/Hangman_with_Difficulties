# Hangman game !
import random

from ISProject import EasWords
from ISProject import NormWords
from ISProject import HardWords


def easy():
    print('easy')


def normal():
    print('normal')


def hard():
    print('hard')


def difficulty():
    while True:
        mode_ui = input('What Difficulty Would You Like To Play?\n(E)asy, (N)ormal {recommended}, or (H)ard: ')

        if mode_ui.lower() == 'n':
            normal()
            break

        elif mode_ui.lower() == 'e':
            easy()
            break

        elif mode_ui.lower() == 'h':
            hard()
            break

        else:
            print('Invalid input, try again.')


difficulty()
