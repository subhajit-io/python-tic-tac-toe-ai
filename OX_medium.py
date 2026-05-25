import random

print("\n\n\nHello user!")
firstname = input("\nMay I know your first name please?: ").capitalize()

print("\nI see... Such a nice name you have", firstname)
choice = input(
    f"\nHey {firstname}, would you like to play a game with me?\n"
    "You can answer me in yes or no only\n No headache!\n "
).lower()

if choice.startswith("y"):
    print("\nAwesome!")
else:
    print("\nOh no! Maybe next time then.")
    exit()

print("\nSo as I can see you said yes, lets play tic tac toe")
variable = input("\nWhat will you choose? O or X?: ").capitalize()

if len(variable) == 0 or variable[0] not in ["X", "O"]:
    variable = "X"

variable = variable[0]
variable2 = "O" if variable == "X" else "X"
print(f"\nOkay so you choose {variable}. I will be {variable2}.")

board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

def display_board():
    print()
    for i in range(3):      
        print(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2])
        if i < 2:
            print("---+---+---")
    print()

display_board()

def get_available_moves(b):
    moves = []
    for i in range(3):
        for j in range(3):
            if b[i][j] not in ["X", "O"]:
                moves.append((i, j))
    return moves

def overwrite(number, b):
    for i in range(3):
        for j in range(3):
            if b[i][j] == number:
                b[i][j] = variable
                print("Your turn: ")
                display_board()
                return True
    return False

def check_winner(b):
    lines = [
        [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
    ]
    for line in lines:
        cells = [b[r][c] for r, c in line]
        if cells[0] == cells[1] == cells[2] and cells[0] in ["X", "O"]:
            return cells[0]
    return None

def ai_simple(b):
    lines = [
        [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
    ]
    
    for line in lines:
        cells = [b[r][c] for r, c in line]
        if cells.count(variable) == 2:
            for r, c in line:
                if b[r][c] not in ["X", "O"]:
                    b[r][c] = variable2
                    print("AI's turn (Blocked you!):")
                    display_board()
                    return

    available = get_available_moves(b)
    if available:
        r, c = random.choice(available)
        b[r][c] = variable2
        print("AI's turn:")
        display_board()

game_over = False
while not game_over:
    valid = False
    while not valid:
        number = input("\nTell me what number you want to play in? ").strip()
        if number not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        if not overwrite(number, board):
            print("That cell is already taken! Pick another one.")
        else:
            valid = True
    winner = check_winner(board)
    if winner:
        print(f"Congratulations! {winner} has won the game!")
        break
    if len(get_available_moves(board)) == 0:
        print("The match has ended with a draw position.")
        break
    ai_simple(board)
    winner = check_winner(board)
    if winner:
        print(f"Congratulations! {winner} has won the game!")
        break
    if len(get_available_moves(board)) == 0:
        print("The match has ended with a draw position.")
        break

print(f"\nThanks for playing, {firstname}!")