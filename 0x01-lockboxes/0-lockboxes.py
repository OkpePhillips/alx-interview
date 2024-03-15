#!/usr/bin/python3
"""
Module to determine if all locked boxes are open
"""


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be opened
    using the provided keys
    """
    n = len(boxes)
    opened = [False] * n

    # Start with the first box (always unlocked by assumption)
    opened[0] = True

    # Iteratively check if keys can open all boxes
    for i in range(n):
        if not opened[i]:
            continue
        current_opened = set()
        current_opened.add(i)
    # Check if keys in the current box can open other boxes
        for key_list in boxes[i]:
            if isinstance(key_list, list):
                for key in key_list:
                    if 0 <= key < n and key not in current_opened:
                        opened[key] = True
                        current_opened.add(key)
            else:
                if 0 <= key_list < n and key_list not in current_opened:
                    opened[key_list] = True
                    current_opened.add(key_list)

    return all(opened)
