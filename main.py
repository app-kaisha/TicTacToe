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

def make_player_move():
    pass


if __name__ == "__main__":
    print("TicTacToe\n")

    players = {
        1: "X",
        2: "O"
    }

    game_board = GameBoard()

    play_game = True
    current_player = 1

    game_board.board[0] = 'X'
    game_board.board[4] = 'X'
    game_board.board[8] = 'X'

    # TODO-1 Inform Players to decide who is X to go first
    print(f'Player {current_player} please select a grid position to place your {players[current_player]}')
    # TODO-2 Ask player to enter grid position for symbol
    player_move = input("Position: ")
    # TODO-3 Check player position is valid
    if game_board.board[int(player_move)] != " ":
        print("Sorry that position is already taken! Select another!")
    else:
        pass
        # TODO-4 Update game board with position
        # TODO-5 Check if win condition exists
        # TODO-6 Change Player
        # TODO-7 Inform Winner
        # TODO-8 Ask to play again
        # TODO-9 Play Again or End game


    display_board(game_board.board)
