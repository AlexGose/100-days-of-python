#!/bin/env python3

from art import logo
from os import system
import random


def deal_cards(cards):
    hands = {
        'player': [draw_card(cards), draw_card(cards)],
        'dealer': [draw_card(cards), draw_card(cards)]
    }
    return hands


def draw_card(cards):
    return random.choice(cards)


def print_cards(hands):
    print(f"Your cards: {hands['player']}, current score: {get_score(hands,'player')}")
    print(f"Computer's first card: {hands['dealer'][0]}")


def hit_person(hands, cards, person):
    hands[person].append(draw_card(cards))
    return hands


def get_score(hands, person):
    if 11 in hands[person] and sum(hands[person]) > 21:
        hands[person].remove(11)
        hands[person].append(1)
    return sum(hands[person])


def is_busted(hands, person):
    return get_score(hands, person) > 21


def print_final_hands(hands):
    print(f"Your final hand: {hands['player']}, final score: {get_score(hands,'player')}")
    print(f"Computer's final hand: {hands['dealer']}, final score: {get_score(hands, 'dealer')}")


def print_winner(hands):
    if is_busted(hands, 'player') or ( not is_busted(hands, 'dealer') and \
            get_score(hands, 'dealer') > get_score(hands, 'player') ) or \
            get_score(hands, 'dealer') == 21:
        print('You lose.')
    elif is_busted(hands, 'dealer') or \
            get_score(hands, 'player') > get_score(hands, 'dealer'):
        print('You win!')
    else:
        print('Draw.')


def clear():
    system('clear')


if __name__ == '__main__':
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    play_game = 'y'
    while play_game == 'y':
        play_message = "Do you want to play a game of Blackjack?"
        play_message += " Type 'y' or 'n': "
        play_game = input(play_message)
        if play_game == 'y':
            clear()
            print(logo)
            hands = deal_cards(cards)
            if get_score(hands, 'dealer') == 21 or \
                    get_score(hands, 'player') == 21:
                print_final_hands(hands)
                print_winner(hands)
                done = True
            else:
                print_cards(hands)
                done = False
            while not done:
                hit = input("Type 'y' to get another card, type 'n' to pass: ")
                if hit == 'y':
                    hands = hit_person(hands, cards, 'player')
                    print_cards(hands)
                    if is_busted(hands, 'player'):
                        print_final_hands(hands)
                        print_winner(hands)
                        done = True
                else:
                    while get_score(hands, 'dealer') < 17:
                        hands = hit_person(hands, cards, 'dealer')
                    print_final_hands(hands)
                    print_winner(hands)
                    done = True
