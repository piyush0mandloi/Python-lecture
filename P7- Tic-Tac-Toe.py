class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
    
    def display_board(self):
        print("\n")
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")  
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("\n")
    
    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        else:
            print("Invalid move! Position already taken.")
            return False
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)              # Diagonal
        ]
        
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False
    
    def check_draw(self):
        return " " not in self.board
    
    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        self.display_board()

        while True:
            try:
                position = int(input(f"Player {self.current_player}, enter position (1-9): ")) - 1
                if position < 0 or position > 8:
                    print("Invalid position. Choose from 1 to 9.")
                    continue
                if self.make_move(position):
                    self.display_board()
                    if self.check_winner():
                        print(f"🎉 Player {self.current_player} wins!")
                        break
                    if self.check_draw():
                        print("It's a draw!")
                        break
                    self.switch_player()
            except ValueError:
                print("Please enter a valid number.")


game = TicTacToe()
game.play_game()