#!/usr/bin/python3
"""
Function to determine if all locked boxes can be opened.
"""


def can_unlock_all(boxes):
    """
    Determines if all locked boxes can be opened.

    Args:
    - boxes: a list of lists where each box may contain keys to other boxes.
             A key with the same number as a box opens that box.

    Returns:
    - True if all boxes can be opened, else False.
    """
  
    unlockedBoxes = [0]
    boxNumber = len(boxes)

    for boxIndex in range(boxNumber):
        for key in boxes[boxIndex]:
            if key is not boxIndex:
                if key > 0 and key < boxNumber and key not in unlockedBoxes:
                    unlockedBoxes.append(key)

    if len(unlockedBoxes) < boxNumber:
        return False
    return True
