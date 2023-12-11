#!/usr/bin/python3
''' This is a lockbox function '''


def canUnlockAll(boxes):
    ''' check if boxes are opened '''
    opened_boxes = set()
    opened_boxes.add(0)

    # Keep track of newly discovered keys
    new_keys = set(boxes[0])

    while new_keys:
        # Update the set of opened boxes with the newly discovered keys
        opened_boxes.update(new_keys)

        # Find new keys in the newly opened boxes
        new_keys = set()
        for key in opened_boxes:
            new_keys.update(boxes[key])

        # Exclude already opened boxes from the set of new keys
        new_keys -= opened_boxes

    return len(opened_boxes) == len(boxes)
