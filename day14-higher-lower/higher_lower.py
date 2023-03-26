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


if __name__ == '__main__':
    print(logo)

    done = False
    while not done:
        # Randomly select two instagram pages
        A_data, B_data = get_insta_pages(data)

        # Print the names of two instagram pages
        print_comparison(A_data, B_data)
        break # temp test code

        # Ask the user which instagram page has more followers

        # If answer is correct, tell user and print current score

        # If answer is wrong, tell user, print final score, and finish loop
