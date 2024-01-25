#!/usr/bin/python3
"""
Module that reads stdin line by line and computes metrics
"""
import sys
import re
from typing import Dict, Tuple

codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
total_file_size = 0
line_processed_count = 0


def print_stats(total_file_size: int, codes: Dict[int, int]) -> None:
    """
    Helper function to print the stats from the computed metrics
    """
    print("File size: {}".format(total_file_size))
    for key, value in codes.items():
        if value > 0:
            print("{}: {}".format(key, value))


def get_line_details(line: str) -> Tuple[str, str]:
    """
    Returns code and file size from line
    """
    # code, file_size = re.search(
    #     r' - \[.*\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)', line)\
    #     .groups()
    split = line.split(" ")
    code = split[-2]
    file_size = split[-1]
    return (code, file_size)


try:
    for line in sys.stdin:
        line_details = get_line_details(line)

        if line_details and len(line_details) > 0:
            code, file_size = line_details
            file_size = int(file_size)

            if code in codes.keys():  # if code exists in codes
                codes[code] += 1  # increment the code count in codes

            line_processed_count += 1  # increment the number of line processed

            total_file_size += file_size  # sum the file size

        if line_processed_count == 10:
            line_processed_count = 0
            print_stats(total_file_size, codes)
except KeyboardInterrupt:
    pass
finally:
    print_stats(total_file_size, codes)
