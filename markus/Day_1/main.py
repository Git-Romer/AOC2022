# Day 1
puzzle = ""
with open("puzzle_input.txt") as file:
    puzzle = file.read().split("\n\n")

elves = []
for entry in puzzle:
    elves.append(sum(int(x) for x in entry.split("\n")))
print(max(elves))