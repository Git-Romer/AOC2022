# Day 1

# load relative os path
import os
path = os.path.dirname(__file__)

# Load data from txt file
dataset = open(os.path.join(path, 'food_supplies.txt'), 'r').readlines()

# Functions
def create_elf_db(data):
    elfcount = 0
    dataset = {}
    for line in data:
        line = line.replace('\n', '')
        elf = f"elf{elfcount + 1}"
        if not line == '':
            if elf in dataset:
                dataset[elf]["calories"].append(line)
            else:
                dataset[elf] = {"calories": [line]}
        else:
            elfcount += 1
            dataset[elf]["sum"] = sum([int(x) for x in dataset[elf]["calories"]])
    dataset[elf]["sum"] = sum([int(x) for x in dataset[elf]["calories"]])
    return dataset

def get_highest_value(dataset):
    highest_value = 0
    for elf in dataset:
        if dataset[elf]["sum"] > highest_value:
            highest_value = dataset[elf]["sum"]
    return highest_value

# Main
if __name__ == "__main__":
    # Create database
    elf_db = create_elf_db(dataset)
    # Get highest value
    highest_value = get_highest_value(elf_db)
    # Print result
    print(f"The highest value is {highest_value}")