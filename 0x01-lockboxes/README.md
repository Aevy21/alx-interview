# Lockbox Unlocking Algorithm

## Introduction

In a scenario where there are multiple locked boxes with keys scattered throughout, the task is to devise an algorithm to determine whether all the boxes can be unlocked, starting with box zero already unlocked. Each box has a unique number and may contain keys to other boxes.

## What is a Lockbox?

A lockbox is a container that holds items securely and can only be opened with a corresponding key. In this context, each lockbox is represented as a numerical index in a list, with each index containing a list of keys corresponding to other lockboxes.

## Checking if Boxes Can be Unlocked

To check if all the boxes can be unlocked, the algorithm utilizes a breadth-first search (BFS) approach. Starting from the initially unlocked box (box zero), it explores each box, marking it as visited, and checks for keys to other boxes. By traversing through the boxes systematically, the algorithm determines whether all boxes can be reached and unlocked.

## Making the Final Decision

The final decision is made based on whether all the boxes are visited during the BFS traversal. If all boxes are visited, it indicates that all boxes can be unlocked, and the algorithm returns True. Otherwise, if there are unvisited boxes remaining, it returns False, indicating that not all boxes can be unlocked.

## Default Box Zero Status

In this algorithm, box zero is assumed to be unlocked by default. This means that the unlocking process begins with box zero already accessible, and the algorithm focuses on unlocking the subsequent boxes.

## Usage

The `canUnlockAll(boxes)` function accepts a list of lists representing the lockboxes and their corresponding keys. Each inner list corresponds to a lockbox, containing the indices of the boxes that can be opened with the keys found in that lockbox.

Example usage:

```python
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True
```

This indicates that all boxes in the provided list `boxes` can be unlocked.

## Conclusion

The Lockbox Unlocking Algorithm provides a systematic approach to determine whether all boxes can be unlocked based on the availability of keys and the accessibility of each box. By leveraging breadth-first search, the algorithm efficiently traverses through the boxes, making it suitable for scenarios with large numbers of lockboxes and keys.
