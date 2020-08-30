import random

# ----- Global Variables -----
player1 = 0
player2 = 0

current_player = 1

game_status = True


def main():
    while game_status:
        ask_player(current_player)
        check_winner()
        flip_player()


def flip_player():
    # Access global variable
    global current_player

    # Change the current player
    current_player = 2


def dice_roll():
    diceRoll = random.randint(1, 6)  # Randomly generate a number from 1 - 6
    return diceRoll


def ask_player(player):
    # Access global variable
    global player1
    global player2
    global game_status

    roll = input(f"Player {player}, Roll or Cancel: ")

    if roll.lower() == "roll":
        set_score(player)
    elif roll.lower() == "cancel":
        print("Program terminated, thank you for playing!")
        game_status = False

    while roll.lower() not in ["roll", "cancel"]:
        print("\nPlease try again!")
        roll = input(f"Player {player}, Roll or Cancel: ")
        if roll.lower() == "roll":
            set_score(player)
        elif roll.lower() == "cancel":
            print("Program terminated, thank you for playing!")
            game_status = False


def set_score(player):
    # Access global variable
    global player1
    global player2

    if player == 1:
        player1 = dice_roll()
    else:
        player2 = dice_roll()


def check_winner():
    # Access global variable
    global game_status

    if player2 > 0:
        if player1 > player2:
            print("\nPlayer 1 won!")
            print(f"Player1: {player1} | Player2: {player2}")
        elif player1 < player2:
            print("\nPlayer 2 won!")
            print(f"Player1: {player1} | Player2: {player2}")
        else:
            print("\nIt's a tie!")
            print(f"Player1: {player1} | Player2: {player2}")
        game_status = False


main()
