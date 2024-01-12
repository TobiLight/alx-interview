#!/usr/bin/python3
# File: 0-lockboxes.py
# Author: Oluwatobiloba Light
# Function that determines if all the boxes can be opened if:
# - boxes is a list of lists
# - A key with the same number as a box opens that box
# - You can assume all keys will be positive integers:
# 		- There can be keys that do not have boxes
# - The first box boxes[0] is unlocked


from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Returns True if all boxes can be opened, else return False
    """
    # Set to keep track of opened boxes
    opened_boxes = {0}

    # Queue to explore new boxes
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        # Iterate through keys in the current box
        for key in boxes[current_box]:
            if key not in opened_boxes:
                # Add the new box to the set of opened boxes
                opened_boxes.add(key)
                # Add the new box to the queue for further exploration
                queue.append(key)

    # Check if all boxes can be opened
    return len(opened_boxes) == len(boxes)
