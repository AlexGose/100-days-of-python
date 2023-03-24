#!/bin/env python3

from art import logo
from random import randint

if __name__ == '__main__':
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = randint(1,100)

    difficulty = input("Choose a difficulty.  Type 'easy' or 'hard': ")

    if difficulty.lower() == 'easy':
        num_attempts = 10
    else:
        num_attempts = 5

    done = False
    while not done:
        print(f"You have {num_attempts} attempt", end='')
        if num_attempts > 1:
            print("s", end='')
        print(" remaining to guess the number.")
            
        guess = int(input("Make a guess: "))
        num_attempts -= 1

        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number}.")
            done = True

        if guess != number:
            if num_attempts == 0:
                print("You've run out of guesses, you lose.")
                done = True
            else:
                print("Guess again.")
