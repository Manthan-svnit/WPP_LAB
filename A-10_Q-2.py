import random
def safe_place(board,row,column):
    for i in range(row):
        if board[i] == column or \
            board[i] - i == column - row or \
            board[i] + i == column + row:
            return False
    return True

def solve_n_queens(n=8):
    board = [-1] * n
    solutions = []
    
    def place_queen(row):
        if row == n:
            solutions.append(board[:])
            return
        for column in range(n):
            if safe_place(board , row , column):
                board[row] = column
                place_queen(row + 1)
                board[row] = -1
    place_queen(0)
    return solutions
def print_board(board):
    n = len(board)
    for i in range(n):
        line = ['.'] * n
        if board[i] != -1:
            line[board[i]] = 'Q'
        print(' '.join(line))
    print()

if __name__ == "__main__":
    solutions = solve_n_queens()
    print(f"Total solutions : {len(solutions)}")
    for i , solutions in enumerate(solutions):
        print(f"Solution {i} :")
        print_board(solutions)