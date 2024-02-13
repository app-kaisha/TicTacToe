from art import logo
import os


class GameBoard:
    def __init__(self):
        self.board = [
            " ", " ", " ",
            " ", " ", " ",
            " ", " ", " ",
        ]
        self.player = 0
        self.is_game = True
        self.display_game_board()

    def display_game_board(self):
        print(logo)
        print("\n" + self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("---------")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("---------")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def change_player(self):
        self.player = int(not self.player)

    def get_player_symbol(self):
        return 'X' if self.player == 0 else 'O'

    def validate_move(self):
        print(f'Player {self.player + 1} please select a grid position to place your {self.get_player_symbol()}')
        player_move = int(input("Position: "))
        try:
            if self.board[player_move] != " ":
                print("Sorry that position is already taken! Select another!")
                self.validate_move()
            else:
                self.board[player_move] = self.get_player_symbol()
        except IndexError:
            print("Out of range of game board! Try again.")
            self.validate_move()

    def check_win(self):
        row_win = (self.board[0] == self.board[1] == self.board[2] == self.get_player_symbol()) | \
                  (self.board[3] == self.board[4] == self.board[5] == self.get_player_symbol()) | \
                  (self.board[6] == self.board[7] == self.board[8] == self.get_player_symbol())
        col_win = (self.board[0] == self.board[3] == self.board[6] == self.get_player_symbol()) | \
                  (self.board[1] == self.board[4] == self.board[7] == self.get_player_symbol()) | \
                  (self.board[2] == self.board[5] == self.board[8] == self.get_player_symbol())
        diag_win = (self.board[0] == self.board[4] == self.board[8] == self.get_player_symbol()) | \
                   (self.board[2] == self.board[4] == self.board[6] == self.get_player_symbol())
        os.system('clear')
        self.display_game_board()
        if row_win | col_win | diag_win:
            print(f'winner: {self.get_player_symbol()}\n')
            self.is_game = False
        else:
            self.change_player()
            print("no win\n")


if __name__ == "__main__":

    game = GameBoard()

    game.board[0] = 'X'
    game.board[6] = 'O'
    game.board[2] = 'O'
    game.board[5] = 'X'
    game.board[8] = 'X'

    while game.is_game:
        game.validate_move()
        # TODO-5 Check if win condition exists
        game.check_win()

        # TODO-7 Inform Winner
        # TODO-8 Ask to play again
        # TODO-9 Play Again or End game
