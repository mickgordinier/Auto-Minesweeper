import random 

WHITE_FLAG = '🏳️'

class Minesweeper():
    def __init__(self, board_size:int, num_mines:int):
        self.board_size = board_size
        self.num_mines = num_mines
        self.user_board = []
        self.solution_board = []
        
        self.create_boards(board_size, num_mines)
        
    
    # Creates both the user interactable board and the solution board
    def create_boards(self, board_size: int, num_mines: int):
        # creating new size x size user board
        for i in range(board_size):
            self.user_board.append(["?"]*board_size)
        
        for i in range(board_size):
            self.solution_board.append([0]*board_size)
            
        for i in range(num_mines):
            while True:
                x_pos = random.randint(0,board_size-1)
                y_pos = random.randint(0,board_size-1)
                
                if self.solution_board[x_pos][y_pos] != "X":
                    self.solution_board[x_pos][y_pos] = "X"
                    self.increment_counter_on_surrounding_pieces(x_pos, y_pos)
                    break  # break out of while loop
            
            
    def increment_counter_on_surrounding_pieces(self, x_pos: int, y_pos: int) -> list:
        for updating_x_pos in range(x_pos-1, x_pos+2):
            if updating_x_pos == -1 or updating_x_pos == len(self.solution_board):
                continue
            
            for updating_y_pos in range(y_pos-1, y_pos+2):
                
                if updating_y_pos == -1 or updating_y_pos == len(self.solution_board):
                    continue
                
                # Will skip all spaces with mines
                if self.solution_board[updating_x_pos][updating_y_pos] == "X":
                    continue
                
                self.solution_board[updating_x_pos][updating_y_pos] = self.solution_board[updating_x_pos][updating_y_pos] + 1
        
        return self.solution_board
    
    
    def human_begin_game(self):
        print()
        self.print_board(self.user_board)
        print()
        
        while True:
            """
            print("What would you like to do?")
            print("1. Guess spot")
            print("2. Place Flag")
            print("3. Remove Flag")
            
            user_turn = int(input("Please enter a number: "))
            """
            print()
            
            x_pos = int(input("X Position: "))
            y_pos = int(input("Y Position: "))
            
            true_list_x_pos = len(self.user_board)-1 - y_pos
            true_list_y_pos = x_pos
            
            print(f"Selecting space [{x_pos}, {y_pos}]")
            self.select_space(true_list_x_pos, true_list_y_pos)
            
            total_count = 0
            for row in self.user_board:
                total_count = total_count + row.count("?")
            print(total_count)
            
            if total_count == self.num_mines:
                print("YOU WIN")
                print()
                self.print_board(self.solution_board)
                print()
                return 0
            
            print()
            self.print_board(self.user_board)
            print()
    
    
    
    def select_space(self, x_pos, y_pos):
        if self.solution_board[x_pos][y_pos] == "X":
            print("BOOM! YOU LOSE")
            print()
            self.print_board(self.solution_board)
            print()
            exit()
            
        self.user_board[x_pos][y_pos] = self.solution_board[x_pos][y_pos]
        
        # Show surrounding area if user clicked on a zero
        if self.solution_board[x_pos][y_pos] == 0:
            stack_of_zeros = [[x_pos, y_pos]]
            
            while True:
                [x_pos, y_pos] = stack_of_zeros.pop()
                
                # counterclockwise and no diagonal pieces
                surrounding_pieces = [[x_pos-1, y_pos], [x_pos, y_pos+1], [x_pos+1, y_pos], [x_pos, y_pos-1]]
                
                for piece in surrounding_pieces:
                    piece_x_pos = piece[0]
                    piece_y_pos = piece[1]
                    
                    if piece_x_pos == -1 or piece_x_pos == len(self.solution_board):
                        continue
                    
                    if piece_y_pos == -1 or piece_y_pos == len(self.solution_board):
                        continue
                        
                    if self.solution_board[piece_x_pos][piece_y_pos] == 0 and self.user_board[piece_x_pos][piece_y_pos] == "?":
                        stack_of_zeros.append([piece_x_pos, piece_y_pos])
                        
                # reveal additional space to user
                self.reveal_surrounding_area(x_pos, y_pos)
                
                if len(stack_of_zeros) == 0:
                    break
        
        self.print_board(self.user_board)
    
    
    def reveal_surrounding_area(self, x_pos, y_pos):
        surrounding_pieces = [[x_pos-1, y_pos], [x_pos, y_pos+1], [x_pos+1, y_pos], [x_pos, y_pos-1]]
        
        for piece in surrounding_pieces:
            search_x_pos = piece[0]
            search_y_pos = piece[1]
                    
            if search_x_pos == -1 or search_x_pos == len(self.solution_board):
                continue
                
            if search_y_pos == -1 or search_y_pos == len(self.solution_board):
                continue
                
            # reveal additional space to user
            self.user_board[search_x_pos][search_y_pos] = self.solution_board[search_x_pos][search_y_pos]

    
    def print_board(self, board: list):
        for x_pos in range(len(board)):
            print("-"*(4*len(board)+1))
            row = ""
            for y_pos in range(len(board)):
                row = row + "| " + str(board[x_pos][y_pos]) + " "
            print(row + "|")
        print("-"*(4*len(board)+1))
        
        
    def place_flag(self, x_pos, y_pos):
        if self.user_board[x_pos][y_pos] != "?":
            print("Invalid Flag Placement")
        else:
            self.user_board[x_pos][y_pos] = WHITE_FLAG