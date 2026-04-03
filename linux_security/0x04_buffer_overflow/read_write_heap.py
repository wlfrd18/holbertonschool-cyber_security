#!/usr/bin/python3
"""
Script that finds a string in the heap of a running process
and replaces it.
"""

import sys


def usage():
    """Print usage and exit."""
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)


def main():
    """Main function."""
    if len(sys.argv) != 4:
        usage()

    pid = sys.argv[1]
    search_string = sys.argv[2].encode()
    replace_string = sys.argv[3].encode()

    maps_path = "/proc/{}/maps".format(pid)
    mem_path = "/proc/{}/mem".format(pid)

    try:
        heap_start = None
        heap_end = None

        with open(maps_path, "r") as maps:
            for line in maps:
                if "[heap]" in line:
                    addresses = line.split()[0]
                    heap_start = int(addresses.split("-")[0], 16)
                    heap_end = int(addresses.split("-")[1], 16)
                    break

        if heap_start is None:
            usage()

        with open(mem_path, "rb+") as mem:
            mem.seek(heap_start)
            heap = mem.read(heap_end - heap_start)

            index = heap.find(search_string)

            if index == -1:
                usage()

            mem.seek(heap_start + index)

            mem.write(
                replace_string
                .ljust(len(search_string), b'\x00')
                [:len(search_string)]
            )

    except Exception:
        usage()


if __name__ == "__main__":
    main()
