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
    print("Fire:", get_player(player)["Fire"])
    print("Ice: ", get_player(player)["Ice"])
    print("Water: ", get_player(player)["Water"])


def choose_card(player):
    if player == 0:
        return random.randint(0, 5)
    else:
        while True:
            card_choice = int(input("Choose a card\nEnter a number from 1 to 5:"))
            # print ("Array index: ", card_choice-1) #check it picks the correct index in array

            if (0 <= (card_choice - 1) <= 5):
                return (card_choice - 1)
                break

            print("Sorry please enter a number from 1 to 5: ")


def Cards(player):
    playerStr = ""
    if player == 0:
        playerStr = "Computer"
    elif player == 1:
        playerStr = "Player 1"

    print("Card options for", playerStr)  # input
    # if statement for player
    # random selection of cards
    card_numbers = [0, 0, 0, 0, 0]
    card_symbols = [0, 0, 0, 0, 0]

    for x in range(5):
        card_numbers[x] = random.randint(0, 10)
        card_symbols[x] = random.choice(Symbol)
        print((x + 1), ": [", card_symbols[x], "-", card_numbers[x], "]")

    # print(card_numbers)
    # print(card_symbols)

    Your_card = choose_card(player)
    print(playerStr + " chose card ---Element:", card_symbols[Your_card], "Number:", card_numbers[Your_card], "\n")

    # Update card number and symbol chosen
    get_player(player).update({"card_number": card_numbers[Your_card]})
    get_player(player).update({"card_symbol": card_symbols[Your_card]})


def compare_cards(first, second):
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


def End_game(first, second):
    if ((get_player(first)["Fire"] > 3) or (get_player(first)["Ice"] > 3) or (get_player(first)["Water"] > 3)):
        print("Player 1 wins!")
        return True

    elif ((get_player(second)["Fire"] > 3) or (get_player(second)["Ice"] > 3) or (get_player(second)["Water"] > 3)):
        print("Player 2 wins!")
        return True

    elif ((get_player(first)["Fire"] > 0) and (get_player(first)["Ice"] > 0) and (get_player(first)["Water"] > 0)):
        print("Player 1 wins!")
        return True

    elif ((get_player(second)["Fire"] > 0) and (get_player(second)["Ice"] > 0) and (get_player(second)["Water"] > 0)):
        print("Player 2 wins!")
        return True

    else:
        return False


def Start_Game():
    while True:
        score_player(1)
        Cards(1)

        score_player(0)
        Cards(0)
        compare_cards(1, 0)
        # EndGame


# -------------------------------Main----------------------------------------

# Menu()
score_player(1)
Cards(1)
Cards(0)
compare_cards(1, 0)
bool(End_game(1, 0))


