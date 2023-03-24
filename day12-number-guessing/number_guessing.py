#!/bin/env python3

from art import logo
from random import randint

if __name__ == '__main__':
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = randint(1,100)

    print(f"Pssst, the correct answer is {number}") # temp test code

    difficulty = input("Choose a difficulty.  Type 'easy' or 'hard': ")

    if difficulty.lower() == 'easy':
        num_attempts = 10
    else:
        num_attempts = 5
