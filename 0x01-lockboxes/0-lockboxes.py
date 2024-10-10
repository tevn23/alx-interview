#!/usr/bin/python3
"""
Implemeting a method that determines if all the boxes can be opened
"""


def can_unlock_all(boxes):
    """Determines if all boxes can be unlocked."""
    unlocked = {0}  # The set of unlocked boxes
    keys = [0]      # Stack to explore boxes starting from box 0

    while keys:
        current_box = keys.pop()  # Take a box to explore

        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                keys.append(key)

    # Explicitly return True if all boxes are unlocked, else return False
    if len(unlocked) == len(boxes):
        return True
    else:
        return False

