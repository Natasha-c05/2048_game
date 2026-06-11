import random
 
def start_game():
    grid = []
    print("U= up, D= down, L = left, R= right")
 
    for i in range(4):
        grid.append([0] * 4)
 
    # Add two starting tiles before the game loop begins
    add(grid)
    add(grid)
 
    while True:
        for row in grid:
            print(row)
 
        result = condition(grid)
        if result:
            return result
 
        move(grid)
 
def add(grid):
    while True:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        if grid[r][c] == 0:
            grid[r][c] = 2
            return
 
def move(grid):
    user_move = input("Move: ").lower()
    if user_move == "r":
        right_move(grid)
    if user_move == "l":
        left_move(grid)
    if user_move == "u":
        up_move(grid)
    if user_move == "d":
        down_move(grid)
 
def right_move(grid):
    for i in range(4):
        non_zero = [j for j in grid[i] if j != 0]
        grid[i] = [0] * (4 - len(non_zero)) + non_zero
 
    for i in range(4):
        for j in range(3, 0, -1):
            if grid[i][j] == grid[i][j - 1] and grid[i][j] != 0:
                grid[i][j] = grid[i][j] * 2
                grid[i][j - 1] = 0
 
    for i in range(4):
        non_zero = [j for j in grid[i] if j != 0]
        grid[i] = [0] * (4 - len(non_zero)) + non_zero
 
def left_move(grid):
    for i in range(4):
        non_zero = [j for j in grid[i] if j != 0]
        grid[i] = non_zero + [0] * (4 - len(non_zero))
 
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] = grid[i][j] * 2
                grid[i][j + 1] = 0
 
    for i in range(4):
        non_zero = [j for j in grid[i] if j != 0]
        grid[i] = non_zero + [0] * (4 - len(non_zero))
 
def up_move(grid):
    for col in range(4):
        for row in range(1, 4):
            if grid[row][col] != 0:
                non_zero_num = grid[row][col]
                r = row
                while r > 0:
                    if grid[r - 1][col] == 0:
                        grid[r - 1][col] = non_zero_num
                        grid[r][col] = 0
                        r -= 1
                    elif grid[r - 1][col] == non_zero_num:
                        grid[r - 1][col] = non_zero_num * 2  
                        grid[r][col] = 0
                        break
                    else:
                        break
 
def down_move(grid):
    for col in range(4): 
        column = []
        for row in range(4):
            column.append(grid[row][col])
 
        
        non_zero = [v for v in column if v != 0]
        column = [0] * (4 - len(non_zero)) + non_zero
 
        # Merge from bottom up
        for k in range(3, 0, -1):
            if column[k] == column[k - 1] and column[k] != 0: 
                column[k] = column[k] * 2
                column[k - 1] = 0
 
        non_zero = [v for v in column if v != 0]
        column = [0] * (4 - len(non_zero)) + non_zero
 
        for row in range(4):
            grid[row][col] = column[row]
 
def can_merge(grid):
    for i in range(4):
        for j in range(4):
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return True
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return True
    return False
 
def isfull(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False  
    return True  
 
def condition(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                print("You win!")
                return "win" 

    if isfull(grid) and not can_merge(grid):
        print("Game over!")
        return "lose"
    return False
 
print(start_game())
 