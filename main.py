from Minesweeper import *

def main():
    minesweeper = Minesweeper(board_size=6, num_mines=4)
    
    minesweeper.human_begin_game()

    return 0
    
    """
    minesweeper.print_board(minesweeper.user_board)
    
    # first guess
    x_pos = random.randint(0,minesweeper.board_size-1)
    y_pos = random.randint(0,minesweeper.board_size-1)
    minesweeper.select_space(x_pos, y_pos)
    
    while True:
        
        # Find 100% Confident spaces
        for row_idx in range(minesweeper.board_size):
            for col_idx in range(minesweeper.board_size):
                true_list_x_pos = minesweeper.board_size-1 - y_pos
                true_list_y_pos = x_pos
                
                if minesweeper.user_board[row_idx][col_idx] != "?" and minesweeper.user_board[row_idx][col_idx] > 0:
                    
                    min_row = max([0, row_idx-1])
                    max_row = min([minesweeper.board_size, row_idx+1])
                    
                    min_col = max([0, col_idx-1])
                    max_col = min([minesweeper.board_size, col_idx+1])
                    
                    unknown_counter = 0
                    for row in minesweeper.user_board[min_row : max_row]:
                        unknown_counter = unknown_counter + row[min_col : max_col].count("?")
                    
                    if unknown_counter == minesweeper.user_board[row_idx][col_idx]:
                        minesweeper.select_space(row_idx, col_idx)
                    
                    
        print()
        print("NOT WORKING")
        """
main()