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
  
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
