#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    result = 0
    if length != 1:
        for arg in range(1, length):
            result += int(sys.argv[arg])
    print(result)
