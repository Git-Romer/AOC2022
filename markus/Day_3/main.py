# Day 3
puzzle = []
with open("puzzle_input.txt") as file:
    puzzle = file.read().split("\n")

duplicates = []
for i in range(0, len(puzzle), 3):
    for char in puzzle[i]:
        if char in puzzle[i+1] and char in puzzle[i+2]:
            duplicates.append(char)
            break
    
total = 0
for char in duplicates:
    if char.isupper():
        total += ord(char) - 38
    else:
        total += ord(char) - 96
print(total)