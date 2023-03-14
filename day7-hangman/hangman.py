#!/bin/env python3

import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be 
# ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = ['_' for _ in range(len(chosen_word))]

# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

print(hangman_art.logo)
print()
lives_left = 6
while '_' in display and lives_left > 0:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter
    else:
        lives_left -= 1
    print(display)
    print(hangman_art.stages[lives_left])

if lives_left==0:
    print('You lose.')
else:
    print("You win.")
