from math import floor
import pdb
from time import sleep
from datetime import datetime

grid = [
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

    global grid

    for col in range(9):
        if grid[row_num][col] == num:
            return False

    for row in range(9):
        if grid[row][col_num] == num:
            return False

    row_start = floor(row_num / 3) *3
    row_end = row_start + 3
    col_start = floor(col_num / 3) *3
    col_end = col_start + 3
    for row in range(row_start,row_end):
        for col in range(col_start, col_end):
            if grid[row][col] == num:
                return False
        

    return True

def coordinates(position):
    row = floor(position/9)
    column = position % 9
    return (row, column)

def print_grid():
    global grid
    print("---------------")
    for num in range(9):
        print(grid[num])
    print("---------------")

def find_blank():
    global grid
    for pos in range(81):
        row, col = coordinates(pos)
        
        if grid[row][col] == 0:
            return (row, col)
    return None

steps = 0
def solve(depth):
    global grid
    global steps
    steps +=1
    #print(steps)
    #print_grid()
    #print("-"*depth)
    blank = find_blank()

    
    if not blank:
        return True
    row, col = blank
    #sleep(1)
    for number in range(1,10):

        if is_possible(row, col, number):

            grid[row][col] = number
            
            if solve(depth +1):
                return True

    grid[row][col] = 0

    return False
start_time = datetime.now()

solve(1)
end_time = datetime.now()
print("Sollution:")
print_grid()
print(end_time - start_time)
                  