#!/bin/env python3

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('''
        Welcome to Treasure Island.
''')
print('''
        Your mission is to find the treasure.

        You are inside of a castle, trying to find a way out.  There are
        two passage ways.
''')

direction = input("Do you want to go left of right? L or R ")
if direction == 'L':
    print('''
        You go through the passage, outside to the beach, and see an island.
    ''')
    swim_or_wait = input('Do you swim out to the island or wait? S or W ')
    if swim_or_wait == 'W':
        print('''
        A boat comes along the beach and takes you to the island.
        You reach a building with a red, yellow, and blue door.
        ''')
        door = input('Which door do you choose? R Y or B ')
        if door == 'Y':
            print('You win! Congratulations')
        elif door == 'R':
            print('You are burned by fire.  Game over.')
        elif door == 'B':
            print('You are eaten by beasts.  Game over.')
        else:
            print('Game over.')
    else:
        print('You are attacked by sharks.  Game over.')
else:
    print('You fall into a hole.  Game over.')
