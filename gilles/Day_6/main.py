# Day 6

# load relative os path
import os
path = os.path.dirname(__file__)

# Functions
# Load data from txt file
def loader_data():
    import json
    with open(os.path.join(path, 'packet.txt'), 'r') as f:
        dataset = f.read()
    return dataset

# Check when x characters in list are unique
def get_start_of_packet(data, length_of_packet):
    packet_group = []
    for i in range(len(data)):
        packet_group = data[i:i+length_of_packet]
        if len(set(packet_group)) == length_of_packet:
            return i + length_of_packet

# Main
if __name__ == '__main__':
    # Load data
    data = loader_data()
    # Check when 4 characters of strings become different
    start_of_packet_marker = get_start_of_packet(data, 4)
    # Check when 14 characters of strings become different
    start_of_packet_message = get_start_of_packet(data, 14)
    # Print result
    print(f"The start-of-packet marker is at position: {start_of_packet_marker}")
    print(f"The start-of-message marker is at position: {start_of_packet_message}")
