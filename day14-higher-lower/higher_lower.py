#!/bin/env python3

from art import logo, vs
from game_data import data
from random import randint
from os import system


def rand_indices(N, first_index=None):
    """Return two unordered random indices between 0 and N-1, if 
       `first_index == None`.  Otherwise, return a random index other
       than first_index as the second index"""
    if first_index == None:
        first_index = randint(0, N-1)
    second_index = randint(0, N-2)
    if second_index >= first_index:
        second_index += 1
    return first_index, second_index


def get_insta_pages(data, B_dict=None):
    """Return dictionaries for two unordered random instagram pages, if
       `B_dict == None`.  Otherwise, return B_dict as the first instagram page
       and a random instagram page other than B_dict as the second"""
    if B_dict == None:
        A_index, B_index = rand_indices(len(data))
    else:
        B_index = data.index(B_dict)
        A_index, B_index = rand_indices(len(data), first_index=B_index)
    return data[A_index], data[B_index]


def describe(insta_dict):
    """Returns string with name, description, and country of instagram page"""
    return f"{insta_dict['name']}, a {insta_dict['description']}, "\
          +f"from {insta_dict['country']}"


def print_comparison(A_dict, B_dict):
    print(f"Compare A: {describe(A_dict)}.")
    print(vs)
    print(f"Against B: {describe(B_dict)}.")


def answer_is_correct(A_dict, B_dict, answer):
    """
    Return True if answer for most followers is correct, False otherwise
    """
    A_followers = int(A_dict['follower_count'])
    B_followers = int(B_dict['follower_count'])
    if answer == 'A' and A_followers >= B_followers:
        return True
    elif answer == 'B' and B_followers >= A_followers:
        return True
    else:
        return False


def clear_screen():
    system('clear')


if __name__ == '__main__':
    print(logo)

    B_data = None
    score = 0
    done = False
    while not done:
        # Randomly select two instagram pages
        A_data, B_data = get_insta_pages(data, B_data)

        # Print the names of two instagram pages
        print_comparison(A_data, B_data)

        # Ask the user which instagram page has more followers
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        # If answer is correct, tell user and print current score
        if answer_is_correct(A_data, B_data, choice):
            score += 1
            clear_screen()
            print(logo)
            print(f"You're right! Current score: {score}.")
        else: # tell user, print final score, and finish loop
            clear_screen()
            print(logo)
            print(f"Sorry, that's wrong.  Final score: {score}.")
            done = True
