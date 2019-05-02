#!/usr/bin/python3
import sys
if __name__ == "__main__":
    j = 0
    for i in range(1, len(sys.argv)):
        j += int(sys.argv[i])

    print("{}".format(j))
