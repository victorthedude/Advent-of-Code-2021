BORDER = 10

with open("day9/input.txt", 'r') as file:
    heightmap = [[int(char) for char in line.strip('\n')] for line in file]
    #print(heightmap)

low_points = []

### PART 1 ###
def find_neighbours(heightmap, row, col):
    north = heightmap[row - 1][col] if row - 1 >= 0 else BORDER
    west = heightmap[row][col - 1] if col - 1 >= 0 else BORDER
    east = heightmap[row][col + 1] if col + 1 < len(heightmap[row]) else BORDER
    south = heightmap[row + 1][col] if row + 1 < len(heightmap) else BORDER
    return [height for height in [north, west, east, south] if height < BORDER]

sum_risk_level = 0
for row in range(len(heightmap)):
    for col in range(len(heightmap[row])):
        neighbours = find_neighbours(heightmap, row, col)
        current = heightmap[row][col]
        if all(current < neighbour for neighbour in neighbours):
            #print(f"Current [{row}][{col}]: {current}")
            #print(neighbours)
            low_points.append((row, col))
            sum_risk_level += current + 1

### PART 1 ANSWER: 
#print(sum_risk_level)


### PART 2 ###
def rec_determine_basin_size(heightmap, basin_points_set, point):
    row = point[0]
    col = point[1]
    basin_points_set.add(point)

    north = (row - 1, col) if row - 1 >= 0 else (-1, -1)
    west = (row, col - 1) if col - 1 >= 0 else (-1, -1)
    east = (row, col + 1) if col + 1 < len(heightmap[row]) else (-1, -1)
    south = (row + 1, col) if row + 1 < len(heightmap) else (-1, -1)

    neighbours = [tup for tup in [north, west, east, south] if tup != (-1, -1) and heightmap[tup[0]][tup[1]] < 9]
    for t in neighbours:
        neighbour_height = heightmap[t[0]][t[1]]
        if neighbour_height > heightmap[row][col] and t not in basin_points_set and neighbour_height != 9:
            rec_determine_basin_size(heightmap, basin_points_set, t)
    
    return basin_points_set

basins = []
for point in low_points:
    basin = rec_determine_basin_size(heightmap, set(), point)
    basins.append(basin)

### PART 2 ANSWER:
basins.sort(key=len, reverse=True)
result = len(basins[0]) * len(basins[1]) * len(basins[2])
print(result)
