# Day 2
#A ROCK 
#B PAPER
#C SCISSOR
#X WIN
#Y LOSE
#Z DRAW


puzzle = ""
with open("puzzle_input.txt") as file:
    puzzle = file.read().split("\n")

score = 0
for match in puzzle:
    if "Y" in match:
        score += 3
        if "A" in match:
            score += 1
        elif "B" in match:
            score += 2
        elif "C" in match:
            score += 3
    elif "Z" in match:
        score += 6
        if "A" in match:
            score += 2
        elif "B" in match:
            score += 3
        elif "C" in match:
            score += 1
    else:
        if "A" in match:
            score += 3
        elif "B" in match:
            score += 1
        elif "C" in match:
            score += 2

print(score)