#!/usr/bin/python3
'''Script that reads stdin line by line and computes metrics'''


import sys


def print_stats(status_counts, total_size):
    """
    Print statistics based on status counts and total size.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

            # Print statistics after every 10 lines
            if counter == 10:
                counter = 0
                print_stats(cache, total_size)

except Exception as err:
    pass

finally:
    # Print final statistics
    print_stats(cache, total_size)
