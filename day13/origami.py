with open("day13/input.txt", 'r') as file:
    points = []
    instructions = []
    for line in file:
        if line != '\n':
            points.append([int(num) for num in line.strip('\n').split(',')])
        else:
            break
    
    for line in file:
        instructions.append((line.strip('\n').split(' ')[2].split('=')))

#print(points)
#print(instructions)

x_max = max([p[0] for p in points])
y_max = max([p[1] for p in points])
paper_grid = [['.' for i in range(x_max + 1)] for j in range(y_max + 1)]

for p in points:
    paper_grid[p[1]][p[0]] = '#'

for i in instructions:
    axis = i[0]
    fold_line = int(i[1])
    if axis == 'x':
        left = [row[:fold_line] for row in paper_grid]
        right = [row[fold_line + 1:] for row in paper_grid]

        for i in range(len(right)):
            for j in range(len(right[i])):
                if right[i][-j - 1] == '#':
                    left[i][j] = '#'
        paper_grid = left

    elif axis == 'y':
        top = paper_grid[:fold_line]
        bottom = paper_grid[fold_line + 1:]

        for i in range(len(bottom)):
            for j in range(len(bottom[i])):
                if bottom[-i - 1][j] == '#':
                    top[i][j] = '#'
        paper_grid = top

    print(f"After folding along {axis}={fold_line}:")
    count = 0
    for row in paper_grid:
        print(''.join(row))
        for x in row:
            if x == '#':
                count +=1
    print(count)
    print()