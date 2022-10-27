#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program adds two numbers

import random


def main():
    # this is a number guessing game

    # input
    random_number = random.randint(1, 9)  # a number between 1 and 9
    print("Random Number Guessing Game.")
    user_number = input("Enter a number between 0-9: ")

    # process
    try:
        number_int = int(user_number)
        if number_int == random_number:
            print("YAY! You guessed the correct number!")
        else:
            print("Random number was {0}. Try again.".format(random_number))
    except ValueError:
        print("Invalid integer")
    finally:
        print("Thanks for playing")
    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
