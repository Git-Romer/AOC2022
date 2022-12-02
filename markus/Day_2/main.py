# Day 2
#A X ROCK 
#B Y PAPER
#C Z SCISSOR

puzzle = ""
with open("puzzle_input.txt") as file:
    puzzle = file.read().split("\n")
for i in range(len(puzzle)):
    puzzle[i] = puzzle[i].replace("X", "A")
    puzzle[i] = puzzle[i].replace("Y", "B")
    puzzle[i] = puzzle[i].replace("Z", "C")

score = 0
for match in puzzle:
    if match[0] == match[2]:
        score += 3

    if match[2] == "A":
        score += 1
        if match[0] == "C":
            score += 6
        
    elif match[2] == "B":
        score += 2
        if match[0] == "A":
            score += 6
    
    elif match[2] == "C":
        score += 3
        if match[0] == "B":
            score += 6

print(score)