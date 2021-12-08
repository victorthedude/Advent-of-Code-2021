
def main():
    with open("day2/input.txt", 'r') as f:
        horizontal_pos = 0
        depth = 0
        aim = 0

        for line in f:
            input = line.split(' ')
            command = input[0]
            unit = int(input[1])

            if command == "forward":
                horizontal_pos += unit
                depth += (aim*unit)
            elif command == "up":
                aim -= unit
            elif command == "down":
                aim += unit
        
        result = horizontal_pos * depth
        print(result)



if __name__ == "__main__":
    main()