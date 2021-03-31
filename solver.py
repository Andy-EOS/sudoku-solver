"""
Basic sudoku solver for 9 x 9 grids.
"""
from math import floor

GRID = [
    [0,0,0,0,1,0,0,0,0],
    [8,3,0,0,0,0,2,0,0],
    [0,0,0,9,5,0,7,0,4],
    [0,2,0,0,0,0,8,0,1],
    [0,0,0,0,0,0,0,0,0],
    [0,4,0,0,8,1,0,0,0],
    [0,0,9,0,4,0,0,6,0],
    [0,0,6,0,0,0,3,0,2],
    [0,0,0,8,6,0,1,0,0],
]

def is_possible(row_num, col_num, num):
    """
    Determine if the supplied number is valid in the position.
    """
    for col in range(9):
        if GRID[row_num][col] == num:
            return False

    for row in range(9):
        if GRID[row][col_num] == num:
            return False

    row_start = floor(row_num / 3) *3
    row_end = row_start + 3
    col_start = floor(col_num / 3) *3
    col_end = col_start + 3
    for row in range(row_start,row_end):
        for col in range(col_start, col_end):
            if GRID[row][col] == num:
                return False

    return True

def print_grid():
    """
    Print out the grid.
    """
    print("---------------")
    for num in range(9):
        print(GRID[num])
    print("---------------")

def find_blank():
    """
    Return the coordinates return the coordinates of the first blank space.
    """
    for row in range(9):
        for col in range(9):
            if GRID[row][col] == 0:
                return (row, col)
    return None

def solve():
    """
    Main solving routine using a backtracking algorithm.
    """
    blank = find_blank()

    if not blank:
        return True
    row, col = blank

    for number in range(1,10):
        if is_possible(row, col, number):
            GRID[row][col] = number
            if solve():
                return True
    GRID[row][col] = 0

    return False

if __name__ == "__main__":
    solve()
    print("Sollution:")
    print_grid()
