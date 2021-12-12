
# board = double list [ ... [...] ...]
def mark_number(board, number):
    for row in board:
        for i in range(len(row)):
            if row[i] == number:
                row[i] = "X"
                return

def row_bingo(board):
    for row in board:
        if all(num == "X" for num in row):
            return True
    return False

def column_bingo(board):
    for i in range(len(board[0])):
        col = [row[i] for row in board]
        if all(num == "X" for num in col):
            return True
    return False

def is_bingo(board):
    return row_bingo(board) or column_bingo(board)

def final_score(board, num):
    print(num)
    print(board)
    unmarked_sum = sum(sum([int(num) if num != "X" else 0 for num in row]) for row in board)
    score = unmarked_sum * int(num)
    print(score)

def rec_find_last_winner(boards, numbers, num_index):
    num = numbers[num_index]
    if len(boards) <= 1:
        mark_number(boards[0], num)
        if is_bingo(boards[0]):
            return final_score(boards[0], num)
        else:
            return rec_find_last_winner(boards, numbers, num_index + 1)
    else:
        for board in boards:
            mark_number(board, num)
        boards = list(filter(lambda b: not is_bingo(b), boards))
        return rec_find_last_winner(boards, numbers, num_index + 1)

def part_1(f):
    numbers = f.readline().strip('\n').split(',')
    boards = []

    #print(numbers)
    f.readline()

    current_board = []
    for line in f:
        if line == '\n':
            boards.append(current_board)
            current_board = []
        else:
            row = list(filter(lambda r: r != "", line.strip('\n').split(' ')))
            current_board.append(row)
    boards.append(current_board)
    #print(boards)

    for num in numbers:
        for board in boards:
            mark_number(board, num)
            if is_bingo(board):
                return final_score(board, num)
                        
    print("No winner!?")
        
def part_2(f):
    numbers = f.readline().strip('\n').split(',')
    boards = []

    #print(numbers)
    f.readline()

    current_board = []
    for line in f:
        if line == '\n':
            boards.append(current_board)
            current_board = []
        else:
            row = list(filter(lambda r: r != "", line.strip('\n').split(' ')))
            current_board.append(row)
    boards.append(current_board)

    return rec_find_last_winner(boards, numbers, 0)

if __name__ == "__main__":
    INPUT_FILE = "day4/input.txt"
    ## one of the functions should always be commented!
    with open(INPUT_FILE, 'r') as f:
    #    part_1(f)
        part_2(f)