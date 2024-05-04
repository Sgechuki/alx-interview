#!/usr/bin/python3
"""
Task 0: Lockboxes
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes
    can be opened
    """
    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and key != box:
                flag = True
                break
        if not flag:
            return False
    return True
