#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding"""

def validUTF8(data):
    # Number of bytes in the current character
    num_bytes = 0

    # Check each integer in the data set
    for num in data:
        # If it's the start of a new character
        if num_bytes == 0:
            # Count the number of leading 1s in the byte
            mask = 1 << 7
            while mask & num:
                num_bytes += 1
                mask >>= 1

            # If it's an invalid start byte
            if num_bytes == 1 or num_bytes > 4:
                return False

            # If it's a single-byte character
            if num_bytes == 0:
                continue

        # If it's not a start byte
        else:
            # If it's not a continuation byte
            if (num >> 6) != 0b10:
                return False

        # Decrement the number of remaining bytes
        num_bytes -= 1

    # If there are remaining bytes
    if num_bytes > 0:
        return False

    return True
