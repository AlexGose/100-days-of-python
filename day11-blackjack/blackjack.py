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
    your_hand_message = f"    Your cards: {hands['player']}, "
    your_hand_message += f"current score: {get_score(hands,'player')}"
    print(your_hand_message)
    computer_hand_message = f"    Computer's first card: {hands['dealer'][0]}"
    print(computer_hand_message)


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
    your_hand_message = f"Your final hand: {hands['player']}, "
    your_hand_message += f"final score: {get_score(hands,'player')}"
    print(your_hand_message)
    dealer_hand_message = f"Computer's final hand: {hands['dealer']}, "
    dealer_hand_message += f"final score: {get_score(hands, 'dealer')}"
    print(dealer_hand_message)


def print_winner(hands):
    if is_busted(hands, 'player'):
        print('You busted. Sorry, you lose 😭')
    elif get_score(hands, 'dealer') == 21 and len(hands['dealer']) == 2:
        print('Dealer has a blackjack 😮  Sorry, you lose 😢')
    elif get_score(hands, 'player') == 21 and len(hands['player']) == 2:
        print('You have a blackjack.  You win! 😎')
    elif not is_busted(hands, 'dealer') and \
            get_score(hands, 'dealer') > get_score(hands, 'player'):
        print('You lose 😤')
    elif is_busted(hands, 'dealer'):
        print('Dealer busts.  You win! 😁')
    elif get_score(hands, 'player') > get_score(hands, 'dealer'):
        print('You win! 😃')
    else:
        print('Draw 😐')


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
