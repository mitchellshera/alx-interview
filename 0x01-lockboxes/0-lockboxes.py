#!/usr/bin/python3
''' This is a lockbox function '''


def canUnlockAll(boxes):
    ''' check if boxes are opened '''
    # Set to keep track of opened boxes
    opened_boxes = set()
    # The first box is initially opened
    opened_boxes.add(0)

    # Iterate through the keys
    for box_index, keys in enumerate(boxes):
        if box_index in opened_boxes:
            # Mark the current box as opened
            opened_boxes.update(keys)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
