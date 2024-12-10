import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict={row.letter:row.code for (word,row) in data.iterrows()}

def generate_phonetic():
    user_input=input("Enter your word").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError :
        print("This input does not take number as input only alphabet A-Z")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
