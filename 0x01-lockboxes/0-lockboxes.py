#!/usr/bin/python3
"""
Function to determine if all locked boxes can be opened.
"""


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """Determines if all the box items are opened.
    Returns: True if they are all opened; False if not
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
