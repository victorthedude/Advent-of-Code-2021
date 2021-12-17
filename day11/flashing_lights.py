INPUT_PATH = "day11/input.txt"

with open(INPUT_PATH, 'r') as file:
    grid = [[int(c) for c in line.strip('\n')] for line in file]


def flash(grid, row, col):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (row + i) in range(len(grid)) and (col + j) in range(len(grid[r])):
                if (row + i, col + j) != (row, col) and grid[row + i][col + j] != 0:
                    grid[row + i][col + j] += 1
    grid[row][col] = 0

## PART 1:
total_flashes = 0
for _ in range(100):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1

    flashing = True
    while flashing:
        has_flashed = False
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] > 9:
                    flash(grid, r, c)
                    total_flashes += 1
                    has_flashed = True

        if not has_flashed:
            flashing = False

#for line in grid:
#    print(line)

## PART 1 ANSWER:
print(f"Total flashes after 100 steps: {total_flashes}")
print()


## PART 2:
with open(INPUT_PATH, 'r') as file:
    grid = [[int(c) for c in line.strip('\n')] for line in file]

all_has_flashed = False
step = 0
while not all_has_flashed:
    step += 1
    ## DUPLICATED CODE FROM PART 1:
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1

    flashing = True
    while flashing:
        has_flashed = False
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] > 9:
                    flash(grid, r, c)
                    total_flashes += 1
                    has_flashed = True

        if not has_flashed:
            flashing = False
    ##

    if all(not any(x != 0 for x in row) for row in grid):
        for line in grid:
            print(line)
        print(f"After step: {step}")
        all_has_flashed = True        
    


