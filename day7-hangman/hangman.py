#!/bin/env python3

import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = ['_' for _ in range(len(chosen_word))]

print(hangman_art.logo)
print()
lives_left = 6
guessed_letters = ''
while '_' in display and lives_left > 0:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You've already guessed {guess}.")
    else:
        guessed_letters += guess
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = letter
        else:
            lose_message = f"You guessed {guess}. That's not in the word. "
            lose_message += "You lose a life."
            print(lose_message)
            lives_left -= 1
        print(' '.join(display))
        print(hangman_art.stages[lives_left])

if lives_left==0:
    print('You lose.')
else:
    print("You win.")
