#!/usr/bin/python3
# File: 0-lockboxes.py
# Author: Oluwatobiloba Light
# Function that determines if all the boxes can be opened if:
# - boxes is a list of lists
# - A key with the same number as a box opens that box
# - You can assume all keys will be positive integers:
# 		- There can be keys that do not have boxes
# - The first box boxes[0] is unlocked
"""
Lockboxes module.
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Returns True if all boxes can be opened, else return False
    """
    # Set to keep track of opened boxes
    opened_boxes = set([0])
    locked_boxes = set(boxes[0]).difference(set([0]))
    while len(locked_boxes) > 0:
        box_index = locked_boxes.pop()

        if not box_index or box_index >= len(boxes) or box_index < 0:
            continue

        if box_index not in opened_boxes:
            locked_boxes = locked_boxes.union(boxes[box_index])
            opened_boxes.add(box_index)
    return len(opened_boxes) == len(boxes)
