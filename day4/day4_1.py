f = open("input", "r")
lines = []
for line in f:
    lines.append(line)

# initialize nums and board
nums = []
boards = []
temp_board = []
for i in range(len(lines)):
    if i == 0:
        nums = lines[i].split(",")
        i += 2
    if lines[i] == "\n":
        boards.append(temp_board)
        temp_board = []
    else:
        temp_line = lines[i].replace("  ", " ")
        if lines[i][0] == " ":
            temp_line = lines[i][1:]
        temp_board.append(temp_line.replace("\n", "").replace("  ", " ").split(" "))
boards.pop(0)

# convert the boards list to int values instead of strings
for board in range(len(boards)):
    for row in range(len(boards[board])):
        for index in range(len(boards[board][row])):
            boards[board][row][index] = int(boards[board][row][index])

# convert bingo nums to int values 
for i in range(len(nums)):
    nums[i] = int(nums[i])

# chceks one board and returns how long it takes to get a bingo
def check_board(board, num_list):
    row_bingo = 9999
    col_bingo = 9999
    # check each num
    for i in range(len(num_list)):
        # iterate through the rows
        if row_bingo >= 9999:
            for row in range(len(board)):
                for index in range(len(board[row])):
                    if(board[row][index] == num_list[i]):
                        board[row][index] = 0

                if sum(board[row]) == 0:
                    row_bingo = i

        # create board by columns
        columns = [[] for _ in range(5)]
        for row in range(len(board)):
            for index in range(len(board[row])):
                columns[index].append(board[row][index])
        
        if col_bingo >= 9999:
            for row in range(len(columns)):
                for index in range(len(columns[row])):
                    if columns[row][index] == num_list[i]:
                        columns[row][index] = 0

                if sum(columns[row]) == 0:
                    col_bingo = i

    return [board.copy(), min(row_bingo, col_bingo)]

fastest = [0, 99999]
for i in range(len(boards)):
    temp = check_board(boards[i], nums)
    if fastest[1] > temp[1]:
        fastest = temp
    
total = 0
for item in fastest[0]:
    total += sum(item)
print(total * nums[fastest[1]])