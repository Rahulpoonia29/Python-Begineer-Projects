import random

print("Guess the Word")
# name = input("What is your name? ")
name = "Rahul"
print(f"Have a nice game {name}")
turns = 10
failed = 0

words_list = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
]

word = random.choice(words_list)


while turns > 0:
    guess = input("Guess the character:")
    for i in word:
        if guess == i:
            print(i)
            a = 1
        else:
            print("-")
    turns -= 1
    if a == 0:
        print("Incorrect guess")
    elif a == 1:
        print("Correct guess")
        a = 0
