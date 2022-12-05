# Day 5
head = []
tail = []

crates = []
instructions = []
with open("puzzle_input.txt") as file:    
    #Read in the crates
    head = [next(file) for x in range(10)]
    head.pop(9)
    head.pop(8)
    #Prepare the matrix
    for i in range(9):
        crates.append([])
    #Fill the matrix
    head.reverse()
    for i in range(len(head)):
        for x, j in enumerate(range(1, 34, 4)):
            if head[i][j] != " ":
                crates[x].append(head[i][j])
    #Read in the instructions
    tail = file.read().split("\n")
    for i in range(len(tail)):
        instructions.append(tail[i].split(" "))
        instructions[i].pop(4) #to
        instructions[i].pop(2) #from
        instructions[i].pop(0) #move
        #Turning into int for easier function calls later
        for x in range(3):
            instructions[i][x] = int(instructions[i][x])

for instruction in instructions:
    buffer = []
    for movecount in range(instruction[0]):
        buffer.append(crates[instruction[1] - 1].pop())
    while buffer != []:
        crates[instruction[2] - 1].append(buffer.pop(0))

result = []
for i in range(9):
    result.append(crates[i].pop())
print(result)