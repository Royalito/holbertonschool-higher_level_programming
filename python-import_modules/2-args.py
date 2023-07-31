#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("Number of argument(s): 0.")
    elif num_arguments == 1:
        print("Number of argument(s): 1:")
    else:
        print("Number of argument(s): {}:".format(num_arguments))

    for idx, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(idx, arg))
