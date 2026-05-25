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

def check_winner(b):
    lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for line in lines:
        cells = [b[r][c] for r, c in line]
        if cells[0] == cells[1] == cells[2] and cells[0] in ["X", "O"]:
            return cells[0]
    return None

def is_draw(b):
    return check_winner(b) is None and len(get_available_moves(b)) == 0

def minimax(b, is_maximizing):
    winner = check_winner(b)
    if winner == variable2:
        return 10
    if winner == variable:
        return -10
    if len(get_available_moves(b)) == 0:
        return 0

    if is_maximizing:
        best_score = -1000
        for r, c in get_available_moves(b):
            original = b[r][c]
            b[r][c] = variable2
            score = minimax(b, False)
            b[r][c] = original
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for r, c in get_available_moves(b):
            original = b[r][c]
            b[r][c] = variable
            score = minimax(b, True)
            b[r][c] = original
            best_score = min(score, best_score)
        return best_score

def ai(b):
    best_score = -1000
    best_move = None

    for r, c in get_available_moves(b):
        original = b[r][c]
        b[r][c] = variable2
        score = minimax(b, False)
        b[r][c] = original
        if score > best_score:
            best_score = score
            best_move = (r, c)

    if best_move:
        r, c = best_move
        b[r][c] = variable2
        print("AI's turn: ")
        display_board()

def overwrite(number, b):
    for i in range(3):
        for j in range(3):
            if b[i][j] == number:
                b[i][j] = variable
                print("Your turn: ")
                display_board()
                return True
    return False
game_over = False

while not game_over:
    valid = False
    while not valid:
        number = input("\nTell me what number you want to play in? ").strip()
        if len(number) == 0 or number[0] not in "123456789":
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        number = number[0]
        if not overwrite(number, board):
            print("That cell is already taken! Pick another one.")
        else:
            valid = True

    winner = check_winner(board)
    if winner:
        print(f"Congratulations! {winner} has won the game!")
        break

    if is_draw(board):
        print("The match has ended with a draw position.")
        break

    ai(board)

    winner = check_winner(board)
    if winner:
        print(f"Congratulations! {winner} has won the game!")
        break

    if is_draw(board):
        print("The match has ended with a draw position.")
        break

print(f"\nThanks for playing, {firstname}!")