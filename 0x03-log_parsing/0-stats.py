#!/usr/bin/python3
"""
Task 0: Log parsing
Input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>
"""
import re
import sys
from typing import Dict


pattern: str = (
    r'^(\S+)(?: -|\s-\s|\s-)?\s?\[(.*?)\] '
    r'"GET /projects/260 HTTP/1\.1" (\d{3}|[A-Za-z]+) (\d+)$'
)
n_line: int = 0
t_size: int = 0
stat_code = {}


def print_stats(t_size: int, stat_code: Dict[int, int]) -> None:
    """
    Print every 10 lines and/or a keyboard interruption
    """
    print("File size: {}".format(t_size))
    sorted_dict = dict(sorted(stat_code.items()))
    for key in sorted_dict:
        print("{}: {}".format(key, sorted_dict[key]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            n_line += 1
            match = re.match(pattern, line.strip())
            if match:
                file_size: int = int(match.group(4))
                try:
                    status_code: int = int(match.group(3))
                    if status_code not in stat_code.keys():
                        stat_code[status_code] = 1
                    else:
                        stat_code[status_code] += 1
                except Exception:
                    pass
                t_size += file_size
            if n_line % 10 == 0:
                print_stats(t_size, stat_code)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(t_size, stat_code)
