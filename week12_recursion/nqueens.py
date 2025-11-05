SOLUTION_NUM = 1

def main():
    num_queens = int(input("Enter the number of queens (4+): "))

    # Setup the Board
    board = []

    for row in range(0, num_queens):
        board.append(['*'] * num_queens)

    solve(board, num_queens, 0)

def solve(board: list[list[str]], num_queens: int, row_num: int):
    if (row_num == len(board)):
        global SOLUTION_NUM
        print(f'Solution {SOLUTION_NUM}:')
        SOLUTION_NUM+=1
        print_board(board)
        print()
    else:
        current_row = board[row_num]
        for col_num in range(len(current_row)):
            if is_safe(board, row_num, col_num):
                current_row[col_num] = 'Q'
                solve(board, num_queens, row_num+1)
                current_row[col_num] = '*'

def is_safe(board: list[list[str]], row_pos: int, col_pos: int) -> bool:

    # check row
    if 'Q' in board[row_pos]:
        return False
    
    # check column
    for row in range(0, len(board)):
        if board[row][col_pos] == 'Q':
            return False
        
    # check upper major diagonal
    i = row_pos
    j = col_pos
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # check upper minor diagonal
    i = row_pos
    j = col_pos
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True









def print_board(board: list[list[str]]) -> None:

    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()










if __name__ == '__main__':
    main()