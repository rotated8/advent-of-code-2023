#!/usr/bin/env python3
import re
from collections import defaultdict

DIGITS = re.compile(r'(\d+)')
GEARS = re.compile(r'\*')

def validate_gears(gears):
    ratios = []
    for gear_key in gears.keys():
        if len(gears[gear_key]) == 2:
            ratios.append(gears[gear_key][0] * gears[gear_key][1])

    print(sum(ratios))

if __name__ == '__main__':
    found_gears = defaultdict(list)
    previous_nums = []
    previous_gears = []

    with open('./input.txt') as inputfile:
        for line in inputfile:
            line = line.strip()
            current_nums = { match for match in DIGITS.finditer(line) }
            current_gears = { match for match in GEARS.finditer(line) }

            for num in current_nums:
                # check current num vs current gears. (match left or right?)
                for gear in current_gears:
                    if num.start() == gear.end() or num.end() == gear.start():
                        found_gears[gear].append(int(num.group()))

                # check current num vs previous gears. (match above?)
                for gear in previous_gears:
                    if num.start() <= gear.end() and num.end() >= gear.start():
                        found_gears[gear].append(int(num.group()))

            for num in previous_nums:
                # check previous line's nums vs current gears. (match below?)
                for gear in current_gears:
                    if num.start() <= gear.end() and num.end() >= gear.start():
                        found_gears[gear].append(int(num.group()))

            previous_nums = current_nums
            previous_gears = current_gears

        validate_gears(found_gears)
