#!/usr/bin/python3
''' This is a lockbox function '''


def canUnlockAll(boxes):
  """
  This function determines if all the boxes can be opened.

  Args:
    boxes: A list of lists, where each inner list contains keys to open other boxes.

  Returns:
    True if all boxes can be opened, False otherwise.
  """
  # Keep track of opened boxes
  opened = set([0])

  # Iterate until no new boxes are opened
  while True:
    new_opened = False
    for i, box in enumerate(boxes):
      if i in opened:
        for key in box:
          if key not in opened and key < len(boxes):
            new_opened = True
            opened.add(key)
    if not new_opened:
      break

  # Check if all boxes are opened
  return len(opened) == len(boxes)
