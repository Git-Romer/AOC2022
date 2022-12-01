# Day 1
puzzle = ""
with open("puzzle_input.txt") as file:
    puzzle = file.read().split("\n\n")

elves = []
for entry in puzzle:
    elves.append(sum(int(x) for x in entry.split("\n")))


total = 0
for i in range(3):
    biggest = max(elves)
    total += biggest
    for j, elf in enumerate(elves):
        if biggest == elf:
           elves.pop(j) 
print(total)