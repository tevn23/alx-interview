#!/usr/bin/python3
"""
Implemeting a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """Method that determines if all boxes can be unlocked"""
     position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
