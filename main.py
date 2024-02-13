

game_board = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " ",
]

def display():
    print(game_board[0] + " | " + game_board[0] + " | " + game_board[0])
    print("---------")
    print(game_board[0] + " | " + game_board[0] + " | " + game_board[0])
    print("---------")
    print(game_board[0] + " | " + game_board[0] + " | " + game_board[0])


if __name__ == "__main__":
    print("TicTacToe")
    display()
