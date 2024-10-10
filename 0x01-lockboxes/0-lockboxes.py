#!/usr/bin/python3
"""
Implemeting a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """Method that determines if all boxes can be unlocked"""
    # Keep track of unlocked boxes with a set
    unlocked = {0} 
    # Stack to process boxes and collect new keys
    keys = [0]
    
    while keys:
        # Get a box from the stack
        current_box = keys.pop()
        # Try to unlock new boxes with the keys from the current box
        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                keys.append(key)
    # If the number of unlocked boxes equals the total number of boxes, return True
    return len(unlocked) == len(boxes)
