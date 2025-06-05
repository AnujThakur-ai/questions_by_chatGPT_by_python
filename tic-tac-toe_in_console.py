# making the board
board = [" " for _ in range(9)]  # a list to hold the board state
#function to print the board
def print_board():
    print("Current board:")
    print(f"{board[0]} \t| {board[1]} \t| {board[2]}")
    print("-------------------------")
    print(f"{board[3]} \t| {board[4]} \t| {board[5]}")
    print("-------------------------")
    print(f"{board[6]} \t| {board[7]} \t| {board[8]}")
    print("\n")
#calling def
print_board()

# to take move
def player_move(player):
    while True:
        move= int (input(f"Player {player}, enter your move (1-9): ")) - 1
        if move <0 and move>8:
            print("Invalid move. please try again.")
        elif board[move] != " ":
            print("That space is already taken. Please try again.")
            continue
        else:
            board[move] = player
            break

player_move(" ")

# to check for a win
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
# to check for a draw
def check_draw():
    return " " not in board
# main game loop
def main():
    current_player = "X"
    while True:
        print_board()
        player_move(current_player)
        
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"
main()