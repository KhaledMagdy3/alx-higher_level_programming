#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    sum = 0
    i = 0
    ac = len(argv)

    for i in range(1, ac):
        sum += int(argv[i])

    print("{:d}".format(sum))
