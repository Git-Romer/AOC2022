# Day 4
puzzle = []
with open("puzzle_input.txt") as file:
    puzzle = file.read().split("\n")

total = 0
for pair in puzzle:
    temp = pair.split(",")
    ll, lh = temp[0].split("-")
    rl, rh = temp[1].split("-")
    ll, lh, rl, rh = int(ll), int(lh), int(rl), int(rh)
    #PERFECT CODE ABOVE
    #INSANE CODE BELOW
    list1 = range(ll, lh+1)
    list2 = range(rl, rh+1)
    for num in list1:
        if num in list2:
            total+=1
            break
        
print(total)