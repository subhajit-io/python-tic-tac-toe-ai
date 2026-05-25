import random
print("\n\n\nHello user!")
firstname = input("\nMay I know your first name please?: ").capitalize()

print("\nI see... Such a nice name you have", firstname)
choice = input(
    f"\nHey {firstname}, would you like to play a game with me?\n"
    "You can answer me in yes or no only\n\nNo headache!\n\n "
).lower()

if choice.startswith("y"):
    print("\nAwesome!")
elif len(choice) == 0:
    print("You typed nothing so I took it as yes!")
    confirmation = input("May be I'm wrong, do you want to exit? ")
    if confirmation.startswith("y"):
        exit()
    else:
        print("Awesome!")
elif choice.startswith("n"):
    print("\nOh no! Maybe next time then.")
    exit()

print("\nSo as I can see you said yes, lets play tic tac toe")
print("\nBut first, choose your difficulty level:")
print("  1 - Easy   ")
print("  2 - Medium ")
print("  3 - Hard   ")

difficulty = input("\nEnter 1, 2, or 3: ").strip()
print(f"Okay so  you picked the {difficulty} number right? ")
if difficulty == "1":
    mode = "easy"
    print("\nYou chose Easy mode.")
elif difficulty == "2":
    mode = "medium"
    print("\nYou chose Medium mode.")
elif difficulty == "3":
    mode = "hard"
    print("\nYou chose Hard mode.")
else:
    mode = "medium"
    print("\nInvalid choice — defaulting to Medium mode.")

variable = input("\nWhat will you choose? O or X?\nFor a random choice hit enter: ").capitalize()

if len(variable) == 0 or variable[0] not in ["X", "O"]:
    variable = random.choice(["O", "X"])

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

WIN_LINES = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

def check_winner(b):
    for line in WIN_LINES:
        cells = [b[r][c] for r, c in line]
        if cells[0] == cells[1] == cells[2] and cells[0] in ["X", "O"]:
            return cells[0]
    return None

def is_draw(b):
    return check_winner(b) is None and len(get_available_moves(b)) == 0

def ai_easy(b):
    available = get_available_moves(b)
    if available:
        r, c = random.choice(available)
        b[r][c] = variable2
        print("AI's turn:")
        display_board()

def ai_medium(b):
    for line in WIN_LINES:
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

def ai_hard(b):
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
        print("AI's turn:")
        display_board()

ai_functions = {
    "easy": ai_easy,
    "medium": ai_medium,
    "hard": ai_hard,
}

ai = ai_functions[mode]

def overwrite(number, b):
    for i in range(3):
        for j in range(3):
            if b[i][j] == number:
                b[i][j] = variable
                print("Your turn: ")
                display_board()
                return True
    return False

def display_scorecard(scores, match_num):
    print("SCORECARD:::")
    print(f"  Matches played : {match_num}")
    print(f"  {firstname} (You)     : {scores['player']} wins")
    print(f"  AI             : {scores['ai']} wins")
    print(f"  Draws          : {scores['draw']}")
    print("\n\n\n")

MAX_MATCHES = 10
scores = {"player": 0, "ai": 0, "draw": 0}

for match_num in range(1, MAX_MATCHES + 1):
    board[0] = ["1", "2", "3"]
    board[1] = ["4", "5", "6"]
    board[2] = ["7", "8", "9"]

    print(f"Match {match_num} of {MAX_MATCHES}-----------------")
    display_board()

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
            if winner == variable:
                print(f"You won Match {match_num}! Well played, {firstname}!")
                scores["player"] += 1
            else:
                print(f"AI won Match {match_num}! Better luck next time.")
                scores["ai"] += 1
            break

        if is_draw(board):
            print(f"Match {match_num} ended in a draw!")
            scores["draw"] += 1
            break

        ai(board)

        winner = check_winner(board)
        if winner:
            if winner == variable:
                print(f"You won Match {match_num}! Well played, {firstname}!")
                scores["player"] += 1
            else:
                print(f"AI won Match {match_num}! Better luck next time.")
                scores["ai"] += 1
            break

        if is_draw(board):
            print(f"Match {match_num} ended in a draw!")
            scores["draw"] += 1
            break

    display_scorecard(scores, match_num)

    if match_num == MAX_MATCHES:
        print(f"\nYou've reached the maximum of {MAX_MATCHES} matches!")
        break

    play_again = input(f"\nWant to play another match? (yes/no): ").strip().lower()
    if play_again.startswith("n"):
        print(f"\nAlright, stopping after {match_num} match(es).")
        break
    elif not play_again.startswith("y"):
        print("I'll take that as a yes! Let's go again!")

print("FINAL RESULTS------------------")
total = scores["player"] + scores["ai"] + scores["draw"]
print(f"  Total matches  : {total}")
print(f"  {firstname} (You)   : {scores['player']} wins")
print(f"  AI             : {scores['ai']} wins")
print(f"  Draws          : {scores['draw']}")
if scores["player"] > scores["ai"]:
    print(f"\nWinner: {firstname}!")
elif scores["ai"] > scores["player"]:
    print(f"\nWinner: AI! Better luck next time!")
else:
    print(f"\nIt's an overall tie!")
print("=" * 35)

print(f"\nThanks for playing, {firstname}! See you next time!")
