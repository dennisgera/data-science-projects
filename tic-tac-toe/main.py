def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

def check_winner(board):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def is_draw(board):
    return " " not in board

print("Welcome to Tic Tac Toe!")
print("The board is numbered like this:")
print_board([str(i) for i in range(1, 10)])
print("Player X starts.")

board = [" " for _ in range(9)]
current_player = "X"
game_over = False

while not game_over:
    print(f"It is player {current_player}'s turn.")
    move = int(input("Where do you want to place your mark? ")) - 1

    if 0 <= move < 9 and board[move] == " ":
        board[move] = current_player
        print_board(board)
        
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            game_over = True
        elif is_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        print("Invalid move. Try again.")

    if game_over:
        new_game = input("Do you want to start a new game? (y/n) ").lower()
        if new_game == "y":
            board = [" " for _ in range(9)]
            current_player = "X"
            game_over = False
            print("Player X starts.")
        else:
            print("Goodbye!")
