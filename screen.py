#!/usr/bin/env python
import os
import signal
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def loop(txt=[], edit=True, c_x=0, c_y=0, blink=True):
    os.system('cls' if os.name == 'nt' else 'clear')

    for i, line in enumerate(txt):
        print(bcolors.OKBLUE + str(i + 1), end=f" {bcolors.OKGREEN}")
        for j, chr in enumerate(line):
            if blink and c_x == i and c_y == j:
                print(bcolors.UNDERLINE + chr, end=f"{bcolors.ENDC}")
            else:
                print(chr, end='')
        print()

    loop(txt, blink=not blink)

    print("\033[94m" + str(len(txt) + 1), end=" \033[92m")
    i = input()
    loop(txt + [i])


if __name__ == "__main__":
    # signal.signal(signal.SIGINT, lambda x, y: None)
    print(os.get_terminal_size().lines)
    loop()
