#!/usr/bin/python3
"""Find a string in the heap of a running process and replace it."""

import ctypes
import os
import sys

PTRACE_ATTACH = 16
PTRACE_DETACH = 17
LIBC = ctypes.CDLL("libc.so.6", use_errno=True)


def usage():
    """Print usage message and exit with status code 1."""
    print("Usage: {} pid search_string replace_string".format(sys.argv[0]))
    sys.exit(1)


def ptrace(request, pid, addr, data):
    """Call ptrace and raise OSError on failure."""
    result = LIBC.ptrace(
        request,
        pid,
        ctypes.c_void_p(addr),
        ctypes.c_void_p(data)
    )
    if result == -1:
        err = ctypes.get_errno()
        raise OSError(err, os.strerror(err))
    return result


def get_heap_range(pid):
    """Return the start and end addresses of the heap."""
    maps_path = "/proc/{}/maps".format(pid)

    with open(maps_path, "r") as maps_file:
        for line in maps_file:
            parts = line.split()
            if parts and parts[-1] == "[heap]":
                start_str, end_str = parts[0].split("-")
                return int(start_str, 16), int(end_str, 16)

    raise ValueError("Heap not found")


def replace_in_heap(pid, search_bytes, replace_bytes):
    """Search and replace all matching strings in the heap."""
    start, end = get_heap_range(pid)
    mem_path = "/proc/{}/mem".format(pid)
    addresses = []

    with open(mem_path, "rb+") as mem_file:
        mem_file.seek(start)
        heap_data = mem_file.read(end - start)

        offset = heap_data.find(search_bytes)
        while offset != -1:
            write_addr = start + offset
            mem_file.seek(write_addr)
            mem_file.write(replace_bytes + b"\x00")
            addresses.append(write_addr)
            offset = heap_data.find(search_bytes, offset + 1)

    if not addresses:
        raise ValueError("search_string not found")

    return addresses


def main():
    """Program entry point."""
    attached = False

    if len(sys.argv) != 4:
        usage()

    pid_arg = sys.argv[1]
    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    if not pid_arg.isdigit():
        usage()

    try:
        search_bytes = search_string.encode("ascii")
        replace_bytes = replace_string.encode("ascii")
    except UnicodeEncodeError:
        print("Error: strings must be ASCII")
        sys.exit(1)

    pid = int(pid_arg)

    try:
        ptrace(PTRACE_ATTACH, pid, 0, 0)
        attached = True
        os.waitpid(pid, 0)

        addresses = replace_in_heap(pid, search_bytes, replace_bytes)
        print("Replaced {} occurrence(s)".format(len(addresses)))

    except Exception as exc:
        print("Error: {}".format(exc))
        sys.exit(1)

    finally:
        if attached:
            try:
                ptrace(PTRACE_DETACH, pid, 0, 0)
            except Exception:
                pass


if __name__ == "__main__":
    main()
