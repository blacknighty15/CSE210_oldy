"""
Tic-Tac-Toe

W02 Prove: Developer - Solo Code Submission

Created by:
Emanuel Herrera

Last updated by 01/12/2021
"""

# Main, game loop, it runs until the game is over
def main():    
    board = new_board()
    player = next_player("")
    while not (check_winner(board) or no_more_moves(board)):
        print_board(board)
        spaces = int(input(f"Player {player} choose a space (1-9): "))
        board[spaces - 1] = player
        player = next_player(player)
    print_board(board)
    print("Thanks for playing!") 

# Prints the board
def print_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print(f"{board[3]}|{board[4]}|{board[5]}")    
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

# Creates a new board
def new_board():
    board = []
    for spaces in range(9):
        board.append(spaces + 1)
    return board

# Checks if there is a winner, prints that a player has won
def check_winner(board):
    if (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6]):
        print(f"Player wins!")
        return True

# Checks if there are no more moves left
def no_more_moves(board):
    for spaces in range(9):
        if board[spaces] != "X" and board[spaces] != "O":
            print("No more moves!")                        
            return False    
    return True 

# Changes the player
def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"

# Runs the main function
if __name__ == "__main__":
    main()