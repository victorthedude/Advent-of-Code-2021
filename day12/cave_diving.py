from collections import Counter

with open("day12/input.txt", 'r') as file:
    lines = [line.strip('\n').split('-') for line in file]

pathings =  {}
for path in lines:
    if path[0] not in pathings:
        pathings.update({ path[0] : set()})
    if path[1] not in pathings:
        pathings.update({ path[1] : set()})
    
    pathings.get(path[0]).add(path[1])
    pathings.get(path[1]).add(path[0])

answer_1 = 0
def rec_find_all_paths(pathings, path, current_cave, visited):
    if current_cave == "end":
        #print(path + ["end"])
        global answer_1
        answer_1 += 1
    else:
        next_visited = visited.copy()
        if current_cave.islower():
            next_visited = visited + [current_cave]
        for next_cave in pathings.get(current_cave):
            if next_cave.isupper() or (next_cave not in visited):
                rec_find_all_paths(pathings, path + [current_cave], next_cave, next_visited)

#rec_find_all_paths(pathings, [], "start", [])
#print(answer_1)


answer_2 = 0
def rec_find_all_paths_part_2(pathings, path, current_cave, visited):
    if current_cave == "end":
        #print(path + ["end"])
        global answer_2
        answer_2 += 1
    else:
        next_visited = visited.copy()
        if current_cave.islower():
            next_visited = visited + [current_cave]
        small_cave_occurences = Counter(next_visited)

        for next_cave in pathings.get(current_cave):
            if next_cave.isupper() or not small_cave_occurences.get(next_cave):
                rec_find_all_paths_part_2(pathings, path + [current_cave], next_cave, next_visited)
            elif (next_cave != "start" and not any(o == 2 for o in small_cave_occurences.values())):
                rec_find_all_paths_part_2(pathings, path + [current_cave], next_cave, next_visited)

rec_find_all_paths_part_2(pathings, [], "start", [])
print(answer_2)