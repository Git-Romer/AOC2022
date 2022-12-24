# Day 8

# load relative os path
import os
path = os.path.dirname(__file__)

# Functions
# Load data from txt file
def loader_data():
    import json
    with open(os.path.join(path, 'trees.txt'), 'r') as f:
        dataset = f.read().splitlines()
        tree_map = [[int(tree) for tree in line] for line in dataset]
    return tree_map

# Loop through every tree and check its visibility from all 4 sides
def check_trees(data):
    count = 0
    for row in data:
        # skip first row
        if row == data[0]:
            continue
        # skip last row
        if row == data[-1]:
            continue
        # skip first and last character
        for tree in range(1, len(row) - 1):
            case = 0
            # check if tree is visible from any of its above trees
            for above in range(len(data[:data.index(row)])):
                if data[above][tree] >= row[tree]:
                    case = 1
                    break
                else:
                    case = 0
            if case == 0:
                # print("Tree at position {} is visible from above".format(tree))
                count += 1
            else:
                # check if tree is visible from left side
                for left in range(tree):
                    if row[left] >= row[tree]:
                        case = 1
                        break
                    else:
                        case = 0
                if case == 0:
                    # print("Tree at position {} is visible from left".format(tree))
                    count += 1
                else:
                    # check if tree is visible from right side
                    for right in range(tree + 1, len(row)):
                        if row[right] >= row[tree]:
                            case = 1
                            break
                        else:
                            case = 0
                    if case == 0:
                        # print("Tree at position {} is visible from right".format(tree))
                        count += 1
                    else:
                        # check if tree is visible from bottom side
                        for bottom in range(data.index(row) + 1, len(data)):
                            if data[bottom][tree] >= row[tree]:
                                case = 1
                                break
                            else:
                                case = 0
                        if case == 0:
                            # print("Tree at position {} is visible from bottom".format(tree))
                            count += 1
                        else:
                            # print("Tree at position {} is not visible from any side".format(tree))
                            continue
    return count

# Add outer layer of trees to count
def add_outer(viscount, data):
    outer = (len(data[0]) - 2) * 2 + len(data) * 2
    return outer + viscount

# Main
if __name__ == '__main__':
    # Load data
    data = loader_data()
    # check visibility of trees
    viscount = check_trees(data)
    print(f"Number of trees visible from any of the 4 sides: {viscount}")
    # add outer layer of trees to count
    viscount = add_outer(viscount, data)
    print(f"Number of trees visible from any of the 4 sides including outer layers: {viscount}")
