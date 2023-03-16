#!/bin/env python3

import os
from art import logo


def clear():
    os.system("clear")


def add_new_bid(bids):
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    bids[name]=int(bid)


def print_winner(bids):
    largest_bid = -1
    best_bidder = ''
    for name in bids:
        if bids[name] > largest_bid:
            largest_bid = bids[name]
            best_bidder = name
    print(f"The winner is {best_bidder} with a bid of ${largest_bid}")


if __name__ == '__main__':
    print(logo)
    print("Welcome to the silent auction program.")
    bids = {}
    done = False
    while not done:
        add_new_bid(bids)
        more = input("Are there any other bidders? Type 'yes' or 'no' ")
        if more.lower() != 'yes':
            done = True
        else:
            clear()
    print_winner(bids)

