import pandas as pd

nato_data_frame = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row['letter']: row['code'] for _, row in nato_data_frame.iterrows()}

done = False
while not done:
    try:
        print([nato_dict[letter.upper()] for letter in input("Enter a word: ")])
    except KeyError:
        print("Sorry, only letters please.")
    else:
        done = True

