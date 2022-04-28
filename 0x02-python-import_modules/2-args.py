#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        end = "arguments."
    elif argc == 1:
        end = "argument:"
    else:
        end = "arguments:"
    print(f"{argc} {end}")
    for arg in range(1, argc + 1):
        print(f"{arg}: {sys.argv[arg]}")
