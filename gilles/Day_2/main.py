# Day 2

# load relative os path
import os
path = os.path.dirname(__file__)

# Functions
# Load data from txt file
def load_data():
    with open(os.path.join(path, 'rps_strategy.txt'), 'r') as f:
        dataset = f.readlines()
    return dataset

# dataset into list
def dataset_to_list(dataset):
    for i in range(len(dataset)):
        dataset[i] = dataset[i].split()
    return dataset

# Calculate the score
def calculate_score_strat1(dataset):
    score = 0
    for i in range(len(dataset)):
        # Draw
        # rock
        if dataset[i][0] == "A" and dataset[i][1] == "X":
            score += draw + rock
        # paper
        elif dataset[i][0] == "B" and dataset[i][1] == "Y":
            score += draw + paper
        # scissors
        elif dataset[i][0] == "C" and dataset[i][1] == "Z":
            score += draw + scissors
        # Win
        # paper beats rock
        elif dataset[i][0] == "A" and dataset[i][1] == "Y":
            score += win + paper
        # scissors beats paper
        elif dataset[i][0] == "B" and dataset[i][1] == "Z":
            score += win + scissors
        # rock beats scissors
        elif dataset[i][0] == "C" and dataset[i][1] == "X":
            score += win + rock
        # Loss
        else:
            if dataset[i][1] == "X":
                score += loss + rock
            elif dataset[i][1] == "Y":
                score += loss + paper
            elif dataset[i][1] == "Z":
                score += loss + scissors
    return score

def calculate_score_strat2(dataset):
    score = 0
    for i in range(len(dataset)):
        # Need to lose
        if dataset[i][1] == "X":
            # Lose against rock
            if dataset[i][0] == "A":
                score += loss + scissors
            # Lose against paper
            if dataset[i][0] == "B":
                score += loss + rock
            # Lose against scissors
            if dataset[i][0] == "C":
                score += loss + paper
        # Need to draw
        elif dataset[i][1] == "Y":
            # Draw against rock
            if dataset[i][0] == "A":
                score += draw + rock
            # Draw against paper
            if dataset[i][0] == "B":
                score += draw + paper
            # Draw against scissors
            if dataset[i][0] == "C":
                score += draw + scissors
        # Need to win
        else:
            # Win against rock
            if dataset[i][0] == "A":
                score += win + paper
            # Win against paper
            if dataset[i][0] == "B":
                score += win + scissors
            # Win against scissors
            if dataset[i][0] == "C":
                score += win + rock
    return score


# Defining variables
loss = 0
draw = 3
win = 6
rock = 1
paper = 2
scissors = 3

# Main
if __name__ == "__main__":
    # Load data
    dataset = load_data()
    # Convert dataset to list
    rps_list = dataset_to_list(dataset)
    # Calculate score for strategy 1
    score1 = calculate_score_strat1(rps_list)
    # Calculate score for strategy 2
    score2 = calculate_score_strat2(rps_list)
    # Print score
    print(f"The score for the first strategy is {score1}")
    print(f"The score for the second strategy is {score2}")