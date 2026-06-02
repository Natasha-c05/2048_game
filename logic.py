import random

def start_game():
    grid=[]

    print("U= up, D= down, L = left, R= right")

    for i in range(4):
        grid.append([0]*4)

        
    add(grid)
    for row in grid:
         print(row)

    move(grid)
    #add(grid)

    for row in grid:
         print(row)
    #return grid


def add(grid):
    while True:
        r=random.randint(0,3)
        c=random.randint(0,3)
        if grid[r][c]==0:
            grid[r][c]=2
            return 
        
def move(grid):
    user_move=input("Move: ").lower()
    if user_move=="r":
        right_move(grid)
    if user_move=="l":
        left_move(grid)

    
    if user_move=="u":
        up_move(grid)

    if user_move=="d":
        down_move(grid)


def right_move(grid):
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

def left_move(grid):
    for i in range(4):
            non_zero = []
            for j in grid[i]:
                if j!=0:
                    non_zero.append(j)
            grid[i]= non_zero + [0]*(4-len(non_zero))
       
       
    for i in range(4):
            for j in range(3):
                if grid[i][j]==grid[i][j-1]:
                        total=grid[i][j]+grid[i][j-1]
                        grid[i][j]= 0
                        grid[i][j-1]=total

    for i in range(4):
            non_zero = []
            for j in grid[i]:
                if j!=0:
                    non_zero.append(j)
            grid[i]=non_zero + [0]*(4-len(non_zero))



def up_move(grid):
    for i in range(4):
        for j in range(1,4): # start from row 1 cuz 0 cant move up 
            if grid[i][j]!=0:
                non_zero_num=grid[i][j]
                row=i
                while row>0:
                        if grid[row-1][j]==0:
                             grid[row-1][j]=non_zero_num
                             grid[row][j]=0
                             row-=1
                        elif grid[row-1][j]==non_zero_num:
                             grid[row-1][j]=non_zero_num * non_zero_num
                             grid[row][j]=0
                             break
                        else:
                             break
    return grid

               

def down_move(grid):
    for i in range(4):
        col=[]
        for j in range(4):
            col.append(grid[j][i])
    
        non_zero=[]
        for i in col:
            if i!=0:
                non_zero.append(i)
        col=non_zero + [0] * (4-len(non_zero))

        for k in range(3):
             if col(k)==col(k+1):
                  col[k]= col[k] + col[k+1]
                  col[k+1]=0

        non_zero=[]
        for i in col:
            if i!=0:
                non_zero.append(i)
        col=non_zero + [0] * (4-len(non_zero))

        for i in range(4):
            grid[i][j] = col[i]
    
    print(grid)







print(start_game())


