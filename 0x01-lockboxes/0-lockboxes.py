#!/usr/bin/python3

def canUnlockAll(boxes):
    # Start by unlocking box 0
    unlocked = {0}  # Set of unlocked boxes, initially only box 0 is unlocked
    keys = set(boxes[0])  # Keys found in the first box
    to_check = [0]  # Boxes that we need to explore, starting with box 0

    # Continue unlocking boxes until there are no more boxes to check
    while to_check:
        current_box = to_check.pop()  # Take a box to check
        
        # Check all keys in the current box
        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:  # If valid and not unlocked
                unlocked.add(key)  # Unlock the box
                to_check.append(key)  # Add to boxes to explore
                keys.update(boxes[key])  # Collect new keys from the newly unlocked box
    
    # If the number of unlocked boxes equals the total number of boxes, return True
    return len(unlocked) == len(boxes)
