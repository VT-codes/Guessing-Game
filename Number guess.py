import random

target = random.randint(1, 101)
print("Welcome to the number guessing game.")
print("I am currently thinking....., of a number between 0 and 100, try telling me what it is.")
# print(f"target: {target}")
lives_hard = 5

level = input("What level do you want to play at? 'easy' or 'hard':\n").lower()


def compare(n1, n2):
    if n1 > n2:
        return "Too low."
    else:
        return "Too high."


def game():
    go_on = True
    lives_easy = 10
    lives_hard = 5
    while go_on:
        guess = int(input("Make a guess!\n"))
        if guess == target:
            print("You have guessed it right!")
            go_on = False
        else:
            print(compare(target, guess))
            if level == "easy":
                lives_easy -= 1
                print(f"You have {lives_easy} guesses left.")
                if lives_easy == 0:
                    print(f"You lost, the number was {target}.")
                    go_on = False
            elif level == "hard":
                lives_hard -= 1
                print(f"You have {lives_hard} guesses left.")
                if lives_hard == 0:
                    print(f"You lost, the number was {target}.")
                    go_on = False


if level == "easy":
    print("You have 10 guesses.")
    game()
elif level == "hard":
    print("You have 5 guesses.")
    game()
else:
    print("Please give a valid input.")