#!/usr/bin/python3
import sys

def print_stats(status_counts, total_size):
    """
    Print statistics based on status counts and total size.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            # Split the line into components
            parts = line.split()

            # Check if the line has the expected format
            if len(parts) == 7:
                ip, date, request, status_code, file_size = parts[:5]

                # Extract status code and file size
                status_code = int(status_code)
                file_size = int(file_size)

                # Update total file size
                total_size += file_size

                # Update status code counts
                if status_code in status_counts:
                    status_counts[status_code] += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_stats(status_counts, total_size)

    except KeyboardInterrupt:
        pass  # Handle keyboard interruption gracefully

    finally:
        # Print final statistics
        print_stats(status_counts, total_size)

if __name__ == "__main__":
    main()
