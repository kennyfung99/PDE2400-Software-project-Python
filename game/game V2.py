import random

computer = {
    "card_symbol": "",
    "card_number": -1,
    "Fire": 0,
    "Ice": 0,
    "Water": 0,
}

player1 = {
    "card_symbol": "",
    "card_number": -1,
    "Fire": 0,
    "Ice": 0,
    "Water": 0,
}

player2 = {
    "card_symbol": "",
    "card_number": -1,
    "Fire": 0,
    "Ice": 0,
    "Water": 0,
}

Symbol = ["Fire", "Ice", "Water"]


# -----------------------------------------------------
def Menu():
    print("Welcome to Fire Ice Water!\n\
      1 - How to play\n\
      2 - Start 2 player game \n\
      3 - Start Vs Computer\n\
      4 - Exit")


name = input('What is your name?\n')
print('Hi, %s.' % name)


def get_player(player):
    if player == 0:
        return computer
    elif player == 1:
        return player1
    elif player == 2:
        return player2


def score_player(player):
    print("Player", player, " cards collected:")
    print("Fire:")
    print("Ice: ")
    print("Water: ")


def choose_card(player):
    while True:
        card_choice = int(input("Choose a card\nEnter a number from 1 to 5:"))
        print("Array index: ", card_choice - 1)

        if (0 <= (card_choice - 1) <= 5):
            return (card_choice - 1)
            break

        print("Sorry please enter a number from 1 to 5: ")

# def Elements_score(player):
