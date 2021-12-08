

def main():
    with open("day1/input.txt", 'r') as f:
        i = 0
        first = int(f.readline())
        second = int(f.readline())
        third = int(f.readline())
        sum_A = first + second + third
        first = second
        second = third
        third = int(f.readline())
        sum_B = first + second + third
        print(sum_A)
        print(sum_B)
        print('\n')

        if sum_A < sum_B:
            i += 1

        for line in f:
            #print(line)
            sum_A = sum_B
            first = second
            second = third
            third = int(line)
            sum_B = first + second + third
            
            if sum_A < sum_B:
                i += 1

        print(i)
    

if __name__ == "__main__":
    main()