import random

def start_game():
    grid=[]

    print("U= up, D= down, L = left, R= right")

    for i in range(4):
        grid.append([0]*4)
    add(grid)
    print(grid)
    move(grid)
    add(grid)
    return grid


def add(grid):
    while True:
        r=random.randint(0,3)
        c=random.randint(0,3)
        if grid[r][c]==0:
            grid[r][c]=2
            return 
        
def move(grid):
    user_move=input("Move: ").lower()
    if user_move == "r":
        for i in range(4):
            non_zero = []
            for j in grid[i]:
                if j!=0:
                    non_zero.append(j)
            grid[i]=[0]*(4-len(non_zero)) + non_zero
       
       
        for i in range(4):
            for j in range(3):
                if grid[i][j]==grid[i][j+1]:
                        total=grid[i][j]+grid[i][j+1]
                        grid[i][j]= 0
                        grid[i][j+1]=total

        for i in range(4):
            non_zero = []
            for j in grid[i]:
                if j!=0:
                    non_zero.append(j)
            grid[i]=[0]*(4-len(non_zero)) + non_zero
                        



        







        

            


print(start_game())


