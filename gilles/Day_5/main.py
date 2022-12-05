# Day 5
from copy import deepcopy

# load relative os path
import os
path = os.path.dirname(__file__)

# Functions
# Load data from txt file
def loader_data():
    import json
    with open(os.path.join(path, 'supply_stacks.json'), 'r') as f:
        dataset = json.load(f)
    f.close()
    return dataset

# Convert instructions to list
def convert_instructions(instruction):
    instruction = instruction.split(" ")
    # Remove every string that is not a number
    instruction = [int(i) for i in instruction if i.isdigit()]
    return instruction

# Get apply instruction steps to stacks (CrateMover_9000)
def apply_instruction_CrateMover_9000(data):
    for instruction in data["instructions"]:
        instruction = convert_instructions(instruction)
        # Append last n values to new stack
        data["stacks"][f"{instruction[2]}"] += data["stacks"][f"{instruction[1]}"][-instruction[0]:][::-1]
        # Remove last n values from old stack
        data["stacks"][f"{instruction[1]}"] = data["stacks"][f"{instruction[1]}"][:-instruction[0]]
    return data

# Get every last value of stacks
def get_last_values(data):
    last_values = []
    for stack in data["stacks"]:
        last_values.append(data["stacks"][f"{stack}"][-1])
    return last_values

# Main
if __name__ == '__main__':
    # Load data
    raw_data = loader_data()

    # Apply instructions (part 1)
    result_part1 = get_last_values(apply_instruction_CrateMover_9000(deepcopy(raw_data)))
    # Print results
    print(f"Sequence of Part 1: {result_part1} -> {''.join(result_part1)}")
