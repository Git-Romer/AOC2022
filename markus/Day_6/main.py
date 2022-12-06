# Day 6
puzzle = ""
with open("input.txt") as file:
    puzzle = file.read()

for i in range(13, len(puzzle)):
    if 14 > len(set(puzzle[i-13:i+1])):
        continue
    print(i+1)
    break