# Day 3
puzzle = []
with open("puzzle_input.txt") as file:
    puzzle = file.read().split("\n")


duplicates = []
for sack in puzzle:
    left = slice(0, len(sack)//2)
    right = slice(len(sack)//2, len(sack))
    for char in sack[left]:
        if char in sack[right]:
            duplicates.append(char)
            break
total = 0
for char in duplicates:
    if char.isupper():
        total += ord(char) - 38
    else:
        total += ord(char) - 96
print(total)