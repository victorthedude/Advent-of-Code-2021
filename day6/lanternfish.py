def rec_simulate(current_state, days):
    if days == 0:
        return len(current_state)
    else:
        for i in range(len(current_state)):
            if (current_state[i] == 0):
                current_state[i] = 6
                current_state.append(8)
            else:
                current_state[i] = current_state[i] - 1

        return rec_simulate(current_state, days - 1)

def day1(initial_state):
    print(rec_simulate(initial_state, 80))

def rec_dict_simulate(anglerfishes_dict, days):
    if days == 0:
        return sum(anglerfishes_dict.values())
    else:
        previous = 0
        for key in reversed(anglerfishes_dict.keys()):
            if key == 0:
                anglerfishes_dict.update({ 6 : anglerfishes_dict.get(6) + anglerfishes_dict.get(key) })
                anglerfishes_dict.update({ 8 : anglerfishes_dict.get(8) + anglerfishes_dict.get(key) })
                anglerfishes_dict.update({ key : previous })
            else:
                old_value = anglerfishes_dict.get(key)
                anglerfishes_dict.update({ key : previous })
                previous = old_value

        return rec_dict_simulate(anglerfishes_dict, days - 1)
                
def day2(initial_dict):
    print(rec_dict_simulate(initial_dict, 256))

if __name__ == "__main__":
    INPUT = "day6/input.txt"
    with open(INPUT, 'r') as file:
        initial = [int(num) for num in file.readline().strip('\n').split(',')]
        day1(initial)

        anglerfishes_dict = { x: initial.count(x) for x in range(9) }
        day2(anglerfishes_dict)
