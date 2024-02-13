class GameBoard:
    def __init__(self):
        self.board = [
            " ", " ", " ",
            " ", " ", " ",
            " ", " ", " ",
        ]


def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


if __name__ == "__main__":
    print("TicTacToe")

    game_board = GameBoard()

    play_game = True

    game_board.board[0] = 'X'
    game_board.board[4] = 'X'
    game_board.board[8] = 'X'
    display_board(game_board.board)


