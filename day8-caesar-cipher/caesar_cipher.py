#!/bin/env python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    output = ''
    for letter in text:
        if letter != ' ':
            index = alphabet.index(letter)
            index += shift
            index %= 26
            output += alphabet[index]
        else:
            output += ' '
    print(f"The encoded text is {output}")

if direction.lower() == 'encode':
    encrypt(text, shift)
