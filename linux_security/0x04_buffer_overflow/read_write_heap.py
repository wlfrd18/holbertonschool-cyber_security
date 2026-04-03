#!/usr/bin/python3
"""
Script that finds a string in the heap of a running process
and replaces it with another string.

Usage:
    read_write_heap.py pid search_string replace_string
"""

import sys


def error():
    """
    Prints usage error message and exits with status code 1.
    """
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)


def get_heap_range(pid):
    """
    Retrieves heap start and end addresses from /proc/<pid>/maps.

    Args:
        pid (str): Process ID

    Returns:
        tuple: (start, end) heap addresses as integers
    """
    maps_path = "/proc/{}/maps".format(pid)

    try:
        with open(maps_path, "r") as maps:
            for line in maps:
                if "[heap]" in line:
                    addresses = line.split()[0]
                    start, end = addresses.split("-")
                    return int(start, 16), int(end, 16)
    except Exception:
        error()

    error()


def replace_in_heap(pid, start, end, search, replace):
    """
    Searches and replaces a string inside heap memory.

    Args:
        pid (str): Process ID
        start (int): Heap start address
        end (int): Heap end address
        search (bytes): String to search
        replace (bytes): Replacement string
    """
    mem_path = "/proc/{}/mem".format(pid)

    try:
        with open(mem_path, "rb+") as mem:
            mem.seek(start)
            heap = mem.read(end - start)

            index = heap.find(search)

            if index == -1:
                error()

            mem.seek(start + index)
            mem.write(replace)

    except Exception:
        error()


def main():
    """
    Main function that validates arguments and performs replacement.
    """
    if len(sys.argv) != 4:
        error()

    pid = sys.argv[1]
    search = sys.argv[2].encode()
    replace = sys.argv[3].encode()

    if len(search) != len(replace):
        error()

    start, end = get_heap_range(pid)

    replace_in_heap(pid, start, end, search, replace)


if __name__ == "__main__":
    main()
