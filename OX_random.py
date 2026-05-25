import random
print("\n\n\nHello user!")
firstname=input("\nMay I know your first name please?: ").capitalize()
print(firstname)
print("\nI see... Such a nice name you have",firstname)
choice=input("\nHey "+ str(firstname)+" would you like to play a game with me ?\nYou can answer me in yes or no only\n No headache! \n ").lower()

if choice.startswith("y"):
    print("\nAwesome!")

else:
    print("\nOh no! Maybe next time then.")
    exit()
print("\nSo as I can see you said yes lets play tic tac toe")
variable=input("\nWhat will you choose ? O or  X ?").capitalize()
variable = variable[0]
print("\nOkay so you choose ",variable)
if(variable=="X"):
    variable2="O"
else:
    variable2="X"
board = [
    ["1", "2", "3"],# 00 01 02
    ["4", "5", "6"],# 10 11 12
    ["7", "8", "9"] # 20 21 22
]
def display_board():
    print()
    for i in range(3):      
        print(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2])
        if i < 2:
            print("---+---+---")
    print()

display_board()

def overwrite(number,board):
        for i in range(3):
            for j in range(3):
                if board[i][j]==number:
                    board[i][j]=variable
                    print("Your turn: ")
                    display_board()
                    return True

def ovrw(n,board):
    for i in range(3):
            for j in range(3):
                if board[i][j]==n:
                    board[i][j]=variable2
                    print("AI's turn: ")
                    display_board()
                    return True

def ai(board):
    lines = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)], 
        [(0,2),(1,2),(2,2)], 
        [(0,0),(1,1),(2,2)],  
        [(0,2),(1,1),(2,0)],  
    ]
    for line in lines:
        cells = [board[r][c] for r, c in line]
        if cells.count(variable) == 2:
            for r, c in line:
                if board[r][c] != variable and board[r][c] != variable2:
                    board[r][c] = variable2
                    print("AI's turn: ")
                    display_board()
                    return
    placed = False
    while not placed:
        n = str(random.randint(1, 9))
        placed = ovrw(n, board)
            
while not(
    board[0][0]==board[0][1]==board[0][2] or
    board[1][0]==board[1][1]==board[1][2] or
    board[2][0]==board[2][1]==board[2][2] or
    board[0][0]==board[1][0]==board[2][0] or
    board[0][1]==board[1][1]==board[2][1] or
    board[0][2]==board[1][2]==board[2][2] or
    board[0][0]==board[1][1]==board[2][2] or
    board[0][2]==board[1][1]==board[2][0]
):
    number = input("\nTell me what number you want to play in? ")
    number = number[0]
    overwrite(number, board)
    n = str(random.randint(1, 9))
    ai(board)
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]=="X" or board[0][i]==board[1][i]==board[2][i]=="X":
            print("Congratulations  X has won the game")
            break
        elif board[i][0]==board[i][1]==board[i][2]=="O" or board[0][i]==board[1][i]==board[2][i]=="O":
            print("Congratulatons O has won the game")
            break
        elif board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X":
            print("Congratulations X has won  the game")
            break
        elif  board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O":
            print("Congratulations O has won the game")
            break
        elif board[i][i] not in ["1","2","3","4","5","6","7","8","9"]:
            print("The match has ended with a draw position")
            break