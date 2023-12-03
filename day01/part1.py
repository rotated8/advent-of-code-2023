#!/usr/bin/env python3
import re

# Use these for part one:
#FIRST_DIGIT = re.compile(r'(\d).*')
#LAST_DIGIT = re.compile(r'.*(\d)')
# Use these for part two:
FIRST_DIGIT = re.compile(r'(\d|one|two|three|four|five|six|seven|eight|nine).*')
LAST_DIGIT = re.compile(r'.*(\d|one|two|three|four|five|six|seven|eight|nine)')

DIGITS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def to_int(num):
    if num in DIGITS.keys():
        num = DIGITS[num]

    return int(num)

def trim_to_num(line):
    first = FIRST_DIGIT.search(line)
    last = LAST_DIGIT.search(line)
    
    # test.txt has 'one' as a test case, but it won't match in part one. Avoid failing there.
    if first is None:
        return 0

    tens = to_int(first.group(1))
    ones = to_int(last.group(1))

    return 10*tens + ones

if __name__ == '__main__':
    with open('./input.txt') as inputfile:
        nums = [ trim_to_num(line) for line in inputfile ]
        print(sum(nums)) 
        # test.txt gives  14+43+68+55+56+33+0 = 269 for part 1
        # test.txt gives  14+23+69+46+56+33+11 = 252 for part 1
