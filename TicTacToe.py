from random import randint

class Board:
    def __init__(self, squares):
        self.squares = squares
    
    def get_square_by_coordinates(self, row, column):
        for square in self.squares:
            if square.row == row and square.column == column:
                return square
        return None
    
    def get_empty_squares(self):
        empty_squares = []
        for square in self.squares:
            if square.content == " ":
                empty_squares.append(square)
        return empty_squares
    
    def get_random_empty_square(self):
        empty_squares = self.get_empty_squares()
        index = randint(0, len(empty_squares) - 1)
        return empty_squares[index]

class Square:
    def __init__(self, row, column, content):
        self.row = row
        self.column = column
        self.content = content

def create_board():
    board = Board([])
    for row in range(3):
        for column in range(3):
            square = Square(row, column, " ")
            board.squares.append(square)
    return board

def print_board(board):
    for row in range(3):
        row_values = []
        for column in range(3):
            square = board.get_square_by_coordinates(row, column)
            if square != None:
                row_values.append(square.content)
        print " | ".join(row_values)
        if row != 2:
            print "---------"

def play_random_square_for_computer(board):
    random_square = board.get_random_empty_square()
    random_square.content = "X"

def start_game():
    board = create_board()
    play_random_square_for_computer(board)
    print_board(board)

start_game()

#user input space
#winning boardstate
#end of game - draw
# def random_row(board):
#    return randint(0, len(board) - 1)

# def random_col(board):
#    return randint(0, len(board[0]) - 1)

# AI_chosen_row = random_row(board)
# AI_chosen_col = random_col(board)

# if board[AI_chosen_row][AI_chosen_col] == "X" or board[AI_chosen_row][AI_chosen_col] == "O":
#    AI_chosen_row = random_row(board)
#    AI_chosen_col = random_col(board)
# else:
#    board[AI_chosen_row][AI_chosen_col] = "X"