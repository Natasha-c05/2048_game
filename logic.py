import random

def start_game():
    grid=[]

    for i in range(4):
        grid.append([0]*4)
    add(grid)
    return grid

def add(grid):
    while True:
        r=random.randint(0,3)
        c=random.randint(0,3)
        if grid[r][c]==0:
            grid[r][c]=2
            return 
            


print(start_game())


