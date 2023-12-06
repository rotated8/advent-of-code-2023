#!/usr/bin/env python3
import re

DIGITS = re.compile(r'(\d+)')
SYMBOLS = re.compile(r'[^\d\.]')

def match_cur(num, syms):
    for sym in syms:
        if num.start() == sym.end() or num.end() == sym.start():
            return True
    return False

def match_other(num, syms):
    for sym in syms:
        if num.start() <= sym.end() and num.end() >= sym.start():
            return True
    return False

if __name__ == '__main__':
    found_nums = [0]
    previous_nums = []
    previous_syms = []

    with open('./input.txt') as inputfile:
        for line in inputfile:
            line = line.strip()
            current_nums = { match for match in DIGITS.finditer(line) }
            current_syms = { match for match in SYMBOLS.finditer(line) }
            removals = set()

            for num in current_nums:
                # check current num vs current syms. (match left or right?)
                if match_cur(num, current_syms):
                    found_nums.append(int(num.group()))
                    removals.add(num)
                    continue # Found, don't need to keep checking.

                # check current num vs previous syms. (match above?)
                if match_other(num, previous_syms):
                    found_nums.append(int(num.group()))
                    removals.add(num)

            for num in previous_nums:
                # check previous line's nums vs current syms. (match below?)
                if match_other(num, current_syms):
                    found_nums.append(int(num.group()))

            previous_nums = current_nums - removals # Remove found nums, no need to match again.
            previous_syms = current_syms

        print(sum(found_nums))
