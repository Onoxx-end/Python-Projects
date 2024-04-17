import pandas

#TODO 1. Read the nato_phonetic_alphabet.csv
#TODO 2. Create a dictionary with the letter as the key and the phonetic code as the value.
#TODO 3. Create a function called "NatoEncoder" that takes a word as input and returns the list of phonetic codes.

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def natoEncoder(text):
    user_input = text.upper()
    nato_list = [nato_dict[letter] for letter in user_input]
    return nato_list

print (natoEncoder(input("Enter a word: ")))