# Day 6
puzzle = ""
with open("input.txt") as file:
    puzzle = file.read()

for i in range(3, len(puzzle)):
    if puzzle[i-3] in (puzzle[i-2], puzzle[i-1], puzzle[i]) or puzzle[i-2] in (puzzle[i-1], puzzle[i]) or puzzle[i-1] == puzzle[i]:
        continue
    print(i+1)
    break