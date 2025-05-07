import pandas as pd

file = pd.read_csv("D:/100 Days Of Python/DAY 30/nato.csv")
nato_dict =file.to_dict()
phonetic_dict = {row.letter:row.code for (index,row) in file.iterrows()}
print(phonetic_dict)
while 1:
    try:
        word = input("Enter a word").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
        break
    except KeyError:
        print("Sorry, only letters in the alphabet please")
