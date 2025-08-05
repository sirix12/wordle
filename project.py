from tabulate import tabulate
import requests
from sys import exit
import termcolor


def main():
    n = get_n()
    correct_word = get_word(n)
    for _ in range(5):
        guessed_word = get_guess(n)
        checked = check(correct_word, guessed_word)
        draw_grid(checked)
    print("Correct answer is", correct_word)


# get number of letters from the user
def get_n():
    while True:
        try:
            print("You can select number of letters of wordl word from 3 to 12")
            n = int(input("number of letters: "))
            if 2 < n < 13:
                return n
        except ValueError:
            pass


# request and return a word with n number of letters
def get_word(letters):
    responce = requests.get(f"https://random-word-api.herokuapp.com/word?length={letters}")
    try:
        return responce.json()[0].upper()
    except IndexError:
        exit("ERROR")


# check the user input word
def check(correct_word, user_word):
    if correct_word == user_word:
        exit(termcolor.colored("YOU WON !", 'green'))
    else:
        checked = []
        for x in range(len(user_word)):
            if correct_word[x] == user_word[x]:
                checked.append(termcolor.colored(user_word[x], 'green', attrs=['reverse', 'blink']))
            elif user_word[x] in correct_word:
                checked.append(termcolor.colored(
                    user_word[x], 'yellow', attrs=['reverse', 'blink']))
            else:
                checked.append(termcolor.colored(user_word[x], 'red', attrs=['reverse', 'blink']))
        return checked


# draw a grid
def draw_grid(checked):
    table = []
    table.append(checked)
    print(tabulate(table, tablefmt="psql"))


# gets the user guessed word from user
def get_guess(n):
    while True:
        word = input("Your Guess: ")
        if len(word) == n:
            return word.upper()
        else:
            print(f"Your guess should only include {n} number of letters.")


if __name__ == "__main__":
    main()
