import random


def diff(num, guess):
    diff_value = abs(num - guess)
    big = guess > num
    return diff_value, big


def commenter(num, guess):
    difference, is_big = diff(num, guess)
    if guess == num:
        return "Congrats you guessed the nnumber correctly"
    elif difference <= 5:
        if is_big:
            return "You are very close, decrease the guess"
        else:
            return "You are very close, increase the guess"
    elif difference <= 20:
        if is_big:
            return "You are close, decrease the guess"
        else:
            return "You are close, increase the guess"
    else:
        if is_big:
            return "You are far, decrease the guess"
        else:
            return "You are far, increase the guess"


target_number = random.randint(1, 100)

for i in range(4):
    user_guess = int(input("Enter your guess: "))
    feedback = commenter(target_number, user_guess)
    print(feedback)
