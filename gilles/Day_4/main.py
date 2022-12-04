# Day 4

# load relative os path
import os
path = os.path.dirname(__file__)

# Functions
# Load data from txt file
def load_data():
    with open(os.path.join(path, 'sections.txt'), 'r') as f:
        dataset = f.read().splitlines()
    return dataset

# Convert sections into lists
def convert_data(dataset):
    pairs = {}
    for i in range(len(dataset)):
        elf1, elf2 = dataset[i].split(',')
        pairs["pair" + str(i)] = {
            "elf1": list(range(int(elf1.split('-')[0]), int(elf1.split('-')[1]) + 1)),
            "elf2": list(range(int(elf2.split('-')[0]), int(elf2.split('-')[1]) + 1))
        }
    return pairs

# Check if two lists have common elements
def check_common_elements(list1, list2):
    if set(list1).issubset(list2) or set(list2).issubset(list1):
        return True

# Check if two lists overlap
def check_overlap(list1, list2):
    if set(list1).intersection(list2) or set(list2).intersection(list1):
        return True

# Main
if __name__ == '__main__':
    # Load data
    data = load_data()
    # Convert sections into lists
    pairs = convert_data(data)
    # Check if two lists have common elements
    common_elements = 0
    overlapping_elements = 0
    for i in range(len(pairs)):
        if check_common_elements(pairs["pair" + str(i)]["elf1"], pairs["pair" + str(i)]["elf2"]):
            common_elements += 1
        if check_overlap(pairs["pair" + str(i)]["elf1"], pairs["pair" + str(i)]["elf2"]):
            overlapping_elements += 1
    print(f"Number of common elements: {common_elements}")
    print(f"Number of overlapping elements: {overlapping_elements}")
