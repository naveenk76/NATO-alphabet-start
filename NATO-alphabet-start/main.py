import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict={row.letter:row.code for (word,row) in data.iterrows()}

user_input=input("Enter your word").upper()

output_list=[phonetic_dict[letter] for letter in user_input]

print(output_list)