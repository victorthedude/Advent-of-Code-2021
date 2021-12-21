from collections import Counter

with open("day14/input.txt", 'r') as file:
    template = file.readline().strip('\n')
    file.readline()
    pair_rules = { line.split(' -> ')[0] : line.strip('\n').split(' -> ')[1] for line in file }

char_count = Counter(template)
pair_count = Counter({ key : 0 for key in pair_rules.keys() })
for i in range(len(template) - 1):
    pair = template[i] + template[i+1]
    pair_count[pair] += 1

print("Template: " + template)
for i in range(1, 41):
    updates = Counter({ key : 0 for key in pair_rules.keys() })
    pairs = [p for p in pair_count if pair_count.get(p) > 0]
    for pair in pairs:
        count = pair_count.get(pair)
        new_char = pair_rules.get(pair)
        char_count[new_char] += count

        p1 = pair[0] + new_char
        p2 = new_char + pair[1]
        updates[p1] += count
        updates[p2] += count
        updates[pair] -= count

    pair_count.update(updates)

    if i == 10:
        result = char_count.most_common()
        answer_1 = result[0][1] - result[-1][1]
        print(f"After 10 steps: {answer_1}")
    
    if i == 40:
        result = char_count.most_common()
        answer_2 = result[0][1] - result[-1][1]
        print(f"After 40 steps: {answer_2}")