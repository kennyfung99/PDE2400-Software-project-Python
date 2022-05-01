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


def Cards(player):
    print("Card options for player", player)  # input
    # if statement for player
    # random selection of cards
    card_number = [0, 0, 0, 0, 0]
    card_symbol = [0, 0, 0, 0, 0]

    for x in range(5):
        card_number[x] = random.randint(0, 10)
        card_symbol[x] = random.choice(Symbol)
        print("Element:", card_symbol[x], "Number:", card_number[x], "\n")

    print(card_number)
    print(card_symbol)

    # print (choose_card(1))
    Your_card = choose_card(1)
    print("You chose card ---Element:", card_symbol[Your_card], "Number:", card_number[Your_card], "\n")

    print(get_player(player))  # before update
    get_player(player).update({"card_number": card_number[Your_card]})
    get_player(player).update({"card_symbol": card_symbol[Your_card]})
    print(get_player(player))


def compare_cards(first, second):
    # if second == 0:
    # print("Computer")   ####should probs delete

    if (get_player(first)["card_symbol"] == "Fire" and get_player(second)["card_symbol"] == "Ice"):
        print("Player 1 scores a point")
        get_player(first).update({"Fire": +1})

    elif (get_player(first)["card_symbol"] == "Fire" and get_player(second)["card_symbol"] == "Water"):
        print("Player 2 scores a point")
        get_player(second).update({"Water": +1})

    elif (get_player(first)["card_symbol"] == "Water" and get_player(second)["card_symbol"] == "Fire"):
        print("Player 1 scores a point")
        get_player(first).update({"Water": +1})

    elif (get_player(first)["card_symbol"] == "Water" and get_player(second)["card_symbol"] == "Ice"):
        print("Player 2 scores a point")
        get_player(second).update({"Ice": +1})

    elif (get_player(first)["card_symbol"] == "Ice" and get_player(second)["card_symbol"] == "Water"):
        print("Player 1 scores a point")
        get_player(first).update({"Ice": +1})

    elif (get_player(first)["card_symbol"] == "Ice" and get_player(second)["card_symbol"] == "Fire"):
        print("Player 2 scores a point")
        get_player(second).update({"Fire": +1})


    elif (get_player(first)["card_symbol"] == get_player(second)["card_symbol"]):
        if ((get_player(first)["card_number"]) > (get_player(second)["card_number"])):
            print("Point to player 1")
            get_player(first).update({get_player(first)["card_symbol"]: +1})

        elif (get_player(first)["card_number"] > get_player(second)["card_number"]):
            print("Point to player 1")

        elif (get_player(first)["card_number"] == get_player(second)["card_number"]):
            print("Draw! One point each")


def two_player():
    while True:
        # score_player(1)
        Cards(1)
        Cards(2)
        #


# -------------------------------Main----------------------------------------

# Menu()
Cards(1)
Cards(2)
compare_cards(1, 2)


