# User Stories
# Your goal is to implement the following user stores:

# As a user (AAU), I want to see a welcome message at the start of a game.
# AAU, before being prompted for a move, I want to see the board printed in the console to know what moves have been made.
# AAU, at the beginning of each turn, told whose turn it is: It's player X's turn!
# AAU, I should be prompted to enter a move and be provided an example of valid input ('Enter a valid move (example: A1)').
# AAU, I want to be able to enter my move's column letter in upper or lower case (a/A, b/B, or c/C) to make it easier to enter my move.
# AAU, if I enter a move in an invalid format or try to occupy a cell already taken, I want to see a message chastising me and be re-prompted.
# AAU, after entering a move, I should once again be presented with the updated game board, notified of the current turn, and asked to enter a move for the other player. This process should continue until there is a winner or a tie
# AAU, I should see a message at the end of the game indicating the winner or stating that the game ended in a tie.


class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turn()
        self.render()

    def print_board(self):
      b = self.board
      print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
      """)

    def print_message(self):
        ## If there is a tie: print("Tie game!")
        if self.tie:
            print("Tie game!")
        ## If there is a winner: print(f"{self.winner} wins the game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        ## Otherwise: print(f"It's player {self.turn}'s turn!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        # Call upon print_board
        self.print_board()
        ## Call upon print_message
        self.print_message()

    def get_move(self):
        while True:
            # prompt user for input
            move = input(f"Enter a valid move (example: A1): ").lower()
            # If the input is valid, update the board and break the loop
            if self.is_valid_move(move):
                self.board[move] = self.turn
                break
              # otherwise, print a message notifying the user of the invalid input and allow the loop to continue
            else:
                print("Invalid move. Try again.")

    def is_valid_move(self, move):
        return move in self.board and self.board[move] is None
    
    def check_for_winner(self):
        winning_combinations = [
            ['a1', 'b1', 'c1'], 
            ['a2', 'b2', 'c2'], 
            ['a3', 'b3', 'c3'],  # rows
            ['a1', 'a2', 'a3'], 
            ['b1', 'b2', 'b3'], 
            ['c1', 'c2', 'c3'],  # columns
            ['a1', 'b2', 'c3'], 
            ['a3', 'b2', 'c1']  # diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] and self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                self.winner = self.board[combo[0]]
                break

    def check_for_tie(self):
        if all(self.board[key] is not None for key in self.board) and not self.winner:
            self.tie = True

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

# Instantiate the Game class and invoke the play_game method
if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()