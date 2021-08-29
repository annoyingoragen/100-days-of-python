import pandas

natodataframe=pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict={rowframe.letter : rowframe.code for (index,rowframe) in natodataframe.iterrows()}

word=input("Enter a word: ").upper()
phonetic_list=[ nato_dict[letter] for letter in word ]

print(phonetic_list)
