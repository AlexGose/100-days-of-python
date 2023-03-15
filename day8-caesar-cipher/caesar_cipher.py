#!/bin/env python3

import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(text, shift, direction):
    output = ''
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction.lower() == 'encode':
                index += shift
            elif direction.lower() == 'decode':
                index -= shift
            else:
                print(f"You must choose either 'encode' or 'decode'")
                exit(1)
            index %= 26
            output += alphabet[index]
        else:
            output += letter
    print(f"The {direction}d text is {output}")

done = False
while not done:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    again = input("Run the program again? Type 'yes' or 'no':\n")
    if again != 'yes':
        done = True
