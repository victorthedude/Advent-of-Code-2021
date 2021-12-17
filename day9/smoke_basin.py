BORDER = 10

with open("day9/input.txt", 'r') as file:
    heightmap = [[int(char) for char in line.strip('\n')] for line in file]
    #print(heightmap)

    ### PART 1 ###
    sum_risk_level = 0
    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            north = heightmap[row - 1][col] if row - 1 >= 0 else BORDER
            west = heightmap[row][col - 1] if col - 1 >= 0 else BORDER
            east = heightmap[row][col + 1] if col + 1 < len(heightmap[row]) else BORDER
            south = heightmap[row + 1][col] if row + 1 < len(heightmap) else BORDER

            current = heightmap[row][col]
            if all(current < neighbour for neighbour in [north, west, east, south]):
                sum_risk_level += current + 1
                #print(f"Current [{row}][{col}]: {current}")
    
    print(sum_risk_level)

    ### PART 2 ###
    