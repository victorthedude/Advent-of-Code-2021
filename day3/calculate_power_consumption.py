
def calculate_power_consumption(inputs):
    most_common_bits = []
    for i in range(len(inputs[0])):
        most_common_bits.append(str(find_most_common_bit(inputs, i)))

    least_common_bits = [ str((int(bit)+1) % 2) for bit in most_common_bits ]

    gamma_rate = ''.join(most_common_bits)
    epsilon_rate = ''.join(least_common_bits)
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print("Power Consumption: " + str(power_consumption))

def calculate_life_support_rating(inputs):
    oxygen = calculate_oxygen_generator_rating(inputs, 0)
    CO2_scrubber = calculate_CO2_scrubber_rating(inputs, 0)
    #print(oxygen)
    #print(CO2_scrubber)
    print("Life Support Rating: " + str(oxygen * CO2_scrubber))

def calculate_oxygen_generator_rating(inputs, i):
    if len(inputs) == 1:
        return int(inputs[0], 2)
    else:
        most_common_bit = find_most_common_bit(inputs, i)
        new_inputs = list(filter(lambda l: l[i] == str(most_common_bit), inputs))
        return calculate_oxygen_generator_rating(new_inputs, i + 1)



def calculate_CO2_scrubber_rating(inputs, i):
    if len(inputs) == 1:
        return int(inputs[0], 2)
    else:
        least_common_bit = (find_most_common_bit(inputs, i) + 1) % 2
        new_inputs = list(filter(lambda l: l[i] == str(least_common_bit), inputs))
        return calculate_CO2_scrubber_rating(new_inputs, i + 1)

def find_most_common_bit(inputs, i):
    count_0 = 0
    count_1 = 0

    for input in inputs:
        num = int(input[i])
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        
        if count_0 > len(inputs)/2:
            break
        elif count_1 > len(inputs)/2:
            break

    if count_0 > count_1:
        return 0
    elif count_1 > count_0:
        return 1
    else:
        return 1

def main():
    with open("day3/input.txt", 'r') as f:
        inputs = []
        for line in f:
            inputs.append(line.strip('\n'))
        
        calculate_power_consumption(inputs)
        calculate_life_support_rating(inputs)

if __name__ == "__main__":
    main()