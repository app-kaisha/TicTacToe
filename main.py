import art
import os


class GameBoard:
    IN_GAME = 0
    WIN = 1
    DRAW = 2

    def __init__(self):
        self.result = None
        self.player = 1
        self.board = None

    def display_game_board(self):
        os.system('clear')
        print(art.logo)
        print("\n" + self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("---------")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("---------")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def change_player(self):
        self.player = int(not self.player)
        self.play()

    def get_player_symbol(self):
        return 'X' if self.player == 0 else 'O'

    def get_player_number(self):
        return self.player + 1

    def play(self):
        self.display_game_board()
        print(
            f'Player {self.get_player_number()} please select a grid position to place your {self.get_player_symbol()}')
        self.validate_move()
        self.check_win()

    def reset_game(self):
        self.board = [
            " ", " ", " ",
            " ", " ", " ",
            " ", " ", " ",
        ]
        # self.player = 0
        self.result = self.IN_GAME
        self.change_player()

    def validate_move(self):
        player_move = input("Position: ")
        try:
            if self.board[int(player_move)] != " ":
                print("Sorry that position is already taken! Select another!")
                self.validate_move()
            else:
                self.board[int(player_move)] = self.get_player_symbol()
        except IndexError:
            print("Out of range of game board! Try again.")
            self.validate_move()
        except ValueError:
            print("You must enter a number between 0 to 8")
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

        self.display_game_board()
        if row_win | col_win | diag_win:
            self.result = self.WIN
            self.game_over()
        elif self.board.count(" ") <= 0:
            self.result = self.DRAW
            self.game_over()
        else:
            self.change_player()

    def game_over(self):
        os.system('clear')
        print(art.logo)
        print("\n\n\n")
        self.display_game_board()

        if self.result == self.WIN:
            print(f'\n{art.winner}\n')
            print(f'{self.get_player_symbol()} WINS!\nPlayer {self.get_player_number()} is the winner!\n')
        else:
            print(f'\n{art.draw}')
        play_again = input(
            "\nWould you like to play again?\nEnter 'y' to play again or 'n' to quit.").lower().strip() == 'y'

        if play_again:
            self.reset_game()
        else:
            os.system('clear')
            exit()


def main():
    """ Start game """
    game = GameBoard()
    game.reset_game()


if __name__ == "__main__":
    main()
