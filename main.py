######################################################
################   H A N G M A N    ##################
######################################################


# Imports

from os import system
from words import word_list
import random
from game_art import stages, logo


# Clear console  function
clear = lambda: system("cls")

# Maximum no. of guesses
MAX_CHANCES = 6


# Game variables
selected_word = random.choice(word_list)
should_play = True
chances_left = MAX_CHANCES
guess_array = ["_" for i in selected_word]
play_again = "y"

# Game Functions


def print_array() -> None:
    """Prints the word from the array of characters passed"""
    global guess_array
    print("My Guess : " + "".join(guess_array) + "\n")


def print_stage() -> None:
    """Cleans the console  , while printing the art !"""
    clear()
    print(logo)
    print(stages[chances_left])


def reset_vars() -> None:
    """Resets the game variables"""
    global guess_array, selected_word
    selected_word = random.choice(word_list)
    guess_array = ["_" for i in selected_word]


# Initial setup
clear()


# Uncomment  this  line to cheat ;-)
# print("The selected word is : " + selected_word)


print(logo)
print("\nWelcome to the game. Guess the word to win ...  Good luck !\n")
print(stages[chances_left])


# Game Loop

while should_play:
    print_array()
    input_char = input("Guess a word : ")

    if input_char in selected_word:

        for i in range(len(selected_word)):
            if input_char == selected_word[i]:
                guess_array[i] = input_char

    else:
        chances_left -= 1

    if chances_left <= 0:
        print_stage()
        print(f"You loose. The correct word was {selected_word}")
        play_again = input("Wanna play again ? 'y' or 'n' : ")
        if play_again == "y":
            chances_left = MAX_CHANCES
            print_stage()
            reset_vars()
            should_play = True
        else:
            print("BYE !")
            should_play = False
    elif not "_" in guess_array:
        clear()
        play_again = input("You won the game ! Wanna play again ? 'y' or 'n' : ")
        if play_again == "y":
            chances_left = MAX_CHANCES
            print_stage()
            reset_vars()
            should_play = True
        else:
            print("BYE !")
            should_play = False
    else:
        print_stage()
        should_play = True
