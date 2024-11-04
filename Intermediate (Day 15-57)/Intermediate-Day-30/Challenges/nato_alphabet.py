import pandas
df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row.letter:row.code for (index,row) in df.iterrows()}

def generate_phonetic():
    user_input = input("Enter a Word: ")
    try:
        word_to_nato_alphabet_list = [nato_alphabet_dict[letter] for letter in user_input.upper()]
    except KeyError:
        print(f"Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(word_to_nato_alphabet_list)

generate_phonetic()