#!/usr/bin/python3
"""
canUnlocAll(boxes)
"""


def canUnlockAll(boxes):

    unlocked = {0}
    keys = set(boxes[0])
    to_check = [0]

    while to_check:
        current_box = to_check.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                to_check.append(key)
                keys.update(boxes[key]) 

    return len(unlocked) == len(boxes)
