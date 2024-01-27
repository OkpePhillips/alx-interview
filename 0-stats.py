#!/usr/bin/env python3
"""
Module to accept input from stdin and print out data in various formats.
"""
import sys
import signal


def calculate_metrics(lines):
    """Function to calculate total file size and count of status codes"""
    total_size = 0
    status_counts = {}

    for line in lines:
        components = line.split()
        if len(components) >= 8:
            status_code = components[7]
            file_size = components[8]
            total_size += int(file_size)
            status_code = int(status_code)
            if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

    return total_size, status_counts

def print_data(total_size, status_counts):
    """
    Printing required data.
    """
    print(f'File size: {total_size}')
    for status_code in sorted(status_counts):
        print(f'{status_code}: {status_counts[status_code]}')

def handle_interrupt(signal, frame):
    """
    Printing data after keyboard interrupt.
    """
    total_size, status_counts = calculate_metrics(lines)
    print_data(total_size, status_counts)
    sys.exit(0)

if __name__ == "__main__":
    lines = []
    try:
        signal.signal(signal.SIGINT, handle_interrupt)
        
        i = 1
        for line in sys.stdin:
            lines.append(line.strip())
            if i % 10 == 0:
                total_size, status_counts = calculate_metrics(lines)
                print_data(total_size, status_counts)
            i += 1

    except KeyboardInterrupt:
        total_size, status_counts = calculate_metrics(lines)
        print_data(total_size, status_counts)
        sys.exit(0)
