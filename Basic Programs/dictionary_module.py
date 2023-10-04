from PyDictionary import PyDictionary

dictionary = PyDictionary()

# word = input("Enter the word = ")
word = "robert"

# options = ["Meaning", "Synonym", "Antonym"]
# for place, option in enumerate(options):
#     print(f"Enter {place+1} for {option} of word")
# choice = input()
# choices = {"1": "meaning", "2": "synonym", "3": "antonym"}

x = dictionary.meaning(word)
for i in x:
    print(f"{i} :-")
    for index, meaning in enumerate(x[i]):
        print(f"{index+1} {meaning.capitalize()} ")
    print()

print(dictionary.synonym(word))
print(dictionary.antonym(word))
