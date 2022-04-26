#!/usr/bin/python3
for fd in range(0, 9):
    for ld in range(fd, 10):
        if fd != ld:
            if fd != 8:
                print(f"{fd}{ld}", end=", ")
            else:
                print(f"{fd}{ld}")
