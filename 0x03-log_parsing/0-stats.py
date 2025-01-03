#!/usr/bin/python3
"""
Log Parsing script that reads stdin and computes metrics.
"""

import sys
import signal

# Initialize metrics
total_file_size = 0
status_code_counts = {}
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

def print_stats():
    """Prints the metrics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        print(f"{code}: {status_code_counts[code]}")

try:
    for line in sys.stdin:
        line_count += 1
        try:
            # Parse line components
            parts = line.split()
            if len(parts) < 7:
                continue
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update metrics
            total_file_size += file_size
            if status_code in valid_status_codes:
                if status_code not in status_code_counts:
                    status_code_counts[status_code] = 0
                status_code_counts[status_code] += 1
        except (ValueError, IndexError):
            # Skip lines that are malformed
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print final stats on keyboard interruption
    print_stats()
    raise
