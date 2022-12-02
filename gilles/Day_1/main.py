# Day 1

# load relative os path
import os
path = os.path.dirname(__file__)

# Functions
# Load data from txt file
def load_data():
    with open(os.path.join(path, 'food_supplies.txt'), 'r') as f:
        dataset = f.read()
    return dataset

# Create database
def create_elf_db(data):
    # Split at every double line break
    elf_db = data.split('\n\n')
    # Split at every line break
    elf_db = [x.split('\n') for x in elf_db]
    # Remove empty strings in list of lists
    elf_db = [[y for y in x if y] for x in elf_db]
    # Convert list of lists to dictionary with category "calories"
    elf_db = {f"elf{elf_db.index(x) + 1}": {"calories": x} for x in elf_db}
    return elf_db

# Calculate sum of calories
def get_calories(elf_db):
    for elf in elf_db:
        # Sum of calories
        elf_db[elf]["sum"] = sum([int(x) for x in elf_db[elf]["calories"]])
    return elf_db

# Get highest value
def get_highest_value(elf_db):
    highest_value = 0
    for elf in elf_db:
        if elf_db[elf]["sum"] > highest_value:
            highest_value = elf_db[elf]["sum"]
    return highest_value

# Get top 3 elfes sum of calories
def get_top_3(elf_db):
    top_3 = []
    for elf in elf_db:
        if len(top_3) < 3:
            top_3.append(elf_db[elf]["sum"])
        else:
            top_3.sort()
            if elf_db[elf]["sum"] > top_3[0]:
                top_3[0] = elf_db[elf]["sum"]
    return top_3

# Main
if __name__ == "__main__":
    # Load data
    dataset = load_data()
    # Create database
    elf_db = create_elf_db(dataset)
    # Get calories
    elf_db = get_calories(elf_db)
    # Get highest value
    highest_value = get_highest_value(elf_db)
    # Get top 3
    top_3 = get_top_3(elf_db)
    # Print result
    print(f"The highest value is {highest_value}")
    print(f"The top 3 sum of calories is {sum(top_3)}")
