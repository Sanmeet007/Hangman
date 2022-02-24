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
HINT_NUMBER = 3




# Game variables
selected_dict = random.choice(word_list)
selected_word = ""
selected_hint = ""

should_play = True
chances_left = MAX_CHANCES
guess_array = []
play_again = "y"

def random_index () -> int :
    global selected_word
    return random.randint(0 , len(selected_word) - 1) 


#  Initial  function


def set_words ()-> None : 
    """Sets the intial setups"""
    global selected_dict , selected_hint , guess_array   , selected_word
    selected_word = selected_dict["word"]
    selected_hint = selected_dict["hint"]
    guess_array = []
    
    choices = []

    for i in range(0  , HINT_NUMBER) :
        choices.append(random_index())

    for i in  range(len(selected_word)):
            if i in choices :
                guess_array.append(selected_word[i])
            else :
                guess_array.append("_")



def print_hint () -> None :
    global selected_hint
    print("Wooho your hint : "+selected_hint)

set_words()

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
    global guess_array, selected_word , set_words , selected_dict 
    selected_dict = random.choice(word_list)
    set_words()


# Initial setup
clear()


# Uncomment  this  line to cheat ;-)
# print("The selected word is : " + selected_word)


print(logo)
print("\nWelcome to the game. Guess the word to win ...  Good luck !\n")
print(stages[chances_left])


# Game Loop

while should_play:
    print_hint()
    print_array() 
    input_char = input("Guess a word : ").lower()
    print(input_char , selected_word)
    # print(selected_word)

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
