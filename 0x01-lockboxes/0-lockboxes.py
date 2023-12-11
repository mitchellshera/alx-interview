#!/usr/bin/python3
''' This is a lockbox function '''


def canUnlockAll(boxes):
    ''' check if boxes are opened '''
    opened_boxes = set()
    opened_boxes.add(0)

    for key in opened_boxes.copy():
        # Iterate through the keys in the currently opened boxes
        for box_index in boxes[key]:
            # Update the set of opened boxes
            # with the keys inside the current box
            opened_boxes.add(box_index)

    return len(opened_boxes) == len(boxes)
