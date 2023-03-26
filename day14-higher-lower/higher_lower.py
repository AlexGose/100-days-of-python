#!/bin/env python3

from art import logo, vs
from game_data import data
from random import randint


def rand_indices(N):
    """Return two unordered random indices between 0 and N-1"""
    first_index = randint(0, N-1)
    second_index = randint(0, N-2)
    if second_index >= first_index:
        second_index += 1
    return first_index, second_index


def get_insta_pages(data):
    """Return data for two unordered random instagram pages"""
    A_index, B_index = rand_indices(len(data))
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


if __name__ == '__main__':
    print(logo)

    score = 0
    done = False
    while not done:
        # Randomly select two instagram pages
        A_data, B_data = get_insta_pages(data)

        # Print the names of two instagram pages
        print_comparison(A_data, B_data)

        # Ask the user which instagram page has more followers
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        # If answer is correct, tell user and print current score
        if answer_is_correct(A_data, B_data, choice):
            score += 1
            print(logo)
            print(f"You're right! Current score: {score}.")
        else: # tell user, print final score, and finish loop
            print(logo)
            print(f"Sorry, that's wrong.  Final score {score}.")
            done = True
