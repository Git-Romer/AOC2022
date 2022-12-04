# Day 4
puzzle = []
with open("puzzle_input.txt") as file:
    puzzle = file.read().split("\n")

total = 0
for pair in puzzle:
    temp = pair.split(",")
    ll, lh = temp[0].split("-")
    rl, rh = temp[1].split("-")
    #PERFECT CODE ABOVE
    #INSANE CODE BELOW

    if int(ll) <= int(rl) and int(lh) >= int(rh):
        total += 1
    elif int(ll) >= int(rl) and int(lh) <= int(rh):
        total += 1

print(total)