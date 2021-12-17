with open("day10/input.txt", 'r') as file:
    lines = [line.strip('\n') for line in file]

#openers = ['(', '[', '{', '<']
#closers = [')', ']', '}', '>']

syntax = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

openers = syntax.keys()
closers = syntax.values()

points = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

## PART 1:
illegal_chars = []
leftover_stacks = []

for line in lines:
    opener_stack = []
    parsed = 0
    for char in line:
        parsed += 1
        if char in openers:
            opener_stack.append(char)
        elif char in closers:
            opener = opener_stack.pop()
            if syntax.get(opener) == char:
                continue
            else:
                #print(f"in '{line}', expected {syntax.get(opener)}, but found {char}")
                illegal_chars.append(char)
                break

    if parsed == len(line):
        leftover_stacks.append(opener_stack)

## PART 1 ANSWER:
syntax_error_score = sum(points.get(char) for char in illegal_chars)
print(syntax_error_score)


## PART 2:
points_2 = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

def determine_score(chars):
    score = 0
    for char in chars:
        score *= 5
        score += points_2.get(syntax.get(char))
    return score

all_scores = [determine_score(reversed(stack)) for stack in leftover_stacks]
## PART 2 ANSWER:
middle_score = list(reversed(sorted(all_scores)))[len(all_scores) // 2]
print(middle_score)
