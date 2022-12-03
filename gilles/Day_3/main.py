# Day 3

# load relative os path
import os
path = os.path.dirname(__file__)

# Functions
# Load data from txt file
def load_data():
    with open(os.path.join(path, 'rucksacks.txt'), 'r') as f:
        dataset = f.read().splitlines()
    return dataset

# Split each rucksack in two
def split_rucksacks(dataset):
    rucksacks = {}
    for i in range(len(dataset)):
        firstpart, secondpart = dataset[i][:len(dataset[i])//2], dataset[i][len(dataset[i])//2:]
        rucksacks["rucksack_" + str(i)] = {
            "firstpart": firstpart,
            "secondpart": secondpart
        }
    return rucksacks

#  Find same items in both parts
def find_same_items(rucksacks):
    for rucksack in rucksacks:
        for item in rucksacks[rucksack]["firstpart"]:
            if item in rucksacks[rucksack]["secondpart"]:
                rucksacks[rucksack]["same_items"] = item

# Convert same items to int
def convert_same_items_to_int(rucksacks):
    for rucksack in rucksacks:
        char = ord(rucksacks[rucksack]["same_items"])
        if rucksacks[rucksack]["same_items"].islower():
            chartoint = char - 96
        else:
            chartoint = char - 38
        rucksacks[rucksack]["chartoint"] = chartoint
    return rucksacks

# Calculate the sum of each item (chartoint)
def calculate_sum_of_items(rucksacks):
    sum = 0
    for rucksack in rucksacks:
        sum += rucksacks[rucksack]["chartoint"]
    return sum

# Group the rucksacks in sets of 3
def group_rucksacks(dataset):
    groups = {}
    groupcount = 0
    for i in range(0, len(dataset), 3):
        if i % 3 == 0:
            groups["group_" + str(groupcount)] = {
                "rucksack_1": dataset[i],
                "rucksack_2": dataset[i+1],
                "rucksack_3": dataset[i+2]
            }
        groupcount += 1
    return(groups)

# Find characters that are the same in all 3 rucksacks
def find_same_items_in_all_rucksacks(groups):
    for group in groups:
        for item in groups[group]["rucksack_1"]:
            if item in groups[group]["rucksack_2"] and item in groups[group]["rucksack_3"]:
                groups[group]["same_items"] = item
    return(groups)

# Main
if __name__ == "__main__":
    # Load data
    dataset = load_data()
    # Split rucksacks in two
    rucksacks = split_rucksacks(dataset)
    # Find same items in both parts
    items = find_same_items(rucksacks)
    # Convert same items to int
    rucksacks = convert_same_items_to_int(rucksacks)
    # Calculate the sum of each item (chartoint)
    sum = calculate_sum_of_items(rucksacks)
    print(f"The sum of the items in the first part is: {sum}")

    # Group the rucksacks in sets of 3
    groups = group_rucksacks(dataset)
    # Find characters that are the same in all 3 rucksacks
    groups = find_same_items_in_all_rucksacks(groups)
    # Convert same items to int
    groups = convert_same_items_to_int(groups)
    # Calculate the sum of each item (chartoint)
    sum = calculate_sum_of_items(groups)
    print(f"The sum of the items in the second part is: {sum}")