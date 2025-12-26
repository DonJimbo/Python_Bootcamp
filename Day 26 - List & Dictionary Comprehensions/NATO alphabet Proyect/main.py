import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}.
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words for a word that the user inputs.
guess_input = input("Please write you guessed code:")
letters_guess_input = [n.upper() for n in guess_input]

output = [nato_dict[letter] for letter in letters_guess_input]
print(f'The phonetic codes for your input are: {output}')


