import pandas

date = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in date.iterrows()}
helper = input("Please type your message: ").upper()
answer = [letter for letter in helper]
code_list2 = [dict[letter] for letter in answer if letter in dict]

print(code_list2)
