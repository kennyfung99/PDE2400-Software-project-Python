import random


def Menu():
    print("Welcome to Fire Ice Water!\n\
      1 - How to play\n\
      2 - Start 2 player game \n\
      3 - Start Vs Computer\n\
      4 - Exit")


name = input('What is your name?\n')
print('Hi, %s.' % name)


def choose_card(player):
    while True:
        card_choice = int(input("Choose a card\nEnter a number from 1 to 5:"))
        print("Array index: ", card_choice - 1)

        if (0 <= (card_choice - 1) <= 5):
            return (card_choice - 1)
            break

        print("Sorry please enter a number from 1 to 5: ")


def Cards(player):
    print("Card options for player", player)  # input
    # if statement for player
    # random selection of cards
    card_number = [0, 0, 0, 0, 0]
    card_symbol = [0, 0, 0, 0, 0]
    for x in range(5):
        card_number[x] = random.randint(0, 10)
        card_symbol[x] = random.randint(0, 2)
        print("Element:", card_symbol[x], "Number:", card_number[x], "\n")

    print(card_number)
    print(card_symbol)

    # print (choose_card(1))
    Your_card = choose_card(1)
    print("You chose card ---Element:", card_symbol[Your_card], "Number:", card_number[Your_card], "\n")


"""
def two_player():
  #Cards(1)


"""

# -------------------------------Main----------------------------------------

Menu()
Cards(1)
