import sys
from typing import NoReturn

no_of_tries = 5
word = "lukasz"
used_letter = []
user_word = []


def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes
def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób: ", no_of_tries)
    print("Uyte litery :", used_letter)
    print()

for _ in word:
    user_word.append("_")


while True:
    letter = input("Podaj literę: ")
    used_letter.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("nie ma takiej litery")
        no_of_tries -= 1
        

        if no_of_tries == 0:
            print("Koniec gry")
            sys.exit(0)
    else: 
        for index in found_indexes:
            user_word[index] = letter
        

        if word == "".join(user_word):
            print("Brawo, to jest to słowo!")
            sys.exit(0)
    show_state_of_game()
 