#!/usr/bin/python3
''' This is a lockbox function '''


def canUnlockAll(boxes):
    ''' check if boxes are opened '''
    opened_boxes = set()
    opened_boxes.add(0)

    for box_index, keys in enumerate(boxes[1:], start=1):
        if box_index in opened_boxes:
            opened_boxes.update(keys)

    return len(opened_boxes) == len(boxes)
