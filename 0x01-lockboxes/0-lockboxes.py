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


def canUnlockAll(boxes: List):
    """
    Returns True if all boxes can be opened, else return False
    """
    opened_box = {0}
    queue = [0]

    while queue:
        current_box_idx = queue.pop(0)

        for key in boxes[current_box_idx]:
            if key not in opened_box:
                opened_box.add(key)
                queue.append(key)
            print(opened_box, queue)

    return len(opened_box) == len(boxes)
