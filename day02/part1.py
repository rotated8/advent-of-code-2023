#!/usr/bin/env python3

import sqlite3, re
import pdb

GAME_ID = re.compile(r'\d+$')
RED = re.compile(r'(\d+) red')
BLUE = re.compile(r'(\d+) blue')
GREEN = re.compile(r'(\d+) green')

def extract_data(line):
    game = []

    game_id, _, subsets = line.partition(': ')
    game_id = int(GAME_ID.search(game_id).group())

    subsets = subsets.strip().split('; ')
    for subset in subsets:
        red = RED.search(subset)
        blue = BLUE.search(subset)
        green = GREEN.search(subset)

        if red is not None:
            red = int(red.group(1))
        else:
            red = 0
        if blue is not None:
            blue = int(blue.group(1))
        else:
            blue = 0
        if green is not None:
            green = int(green.group(1))
        else:
            green = 0

        game.append((game_id, red, blue, green))

    return game

def part_one(conn):
    cursor = conn.cursor()

    all_ids = set()
    for row in cursor.execute('SELECT DISTINCT id FROM game'):
        all_ids.add(row['id'])

    illegals = set()
    for row in cursor.execute('SELECT id FROM game WHERE red > 13 OR blue > 14 OR green > 13'):
        illegals.add(row['id'])

    print(sum(all_ids - illegals))

def part_two(conn):
    cursor = conn.cursor()

    game_power = []
    for row in cursor.execute('SELECT MAX(red), MAX(blue), MAX(green) FROM game GROUP BY id'):
        game_power.append(row['MAX(red)'] * row['MAX(blue)'] * row['MAX(green)'])

    print(sum(game_power))


if __name__ == '__main__':
    connection = sqlite3.connect(':memory:')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE game(id, red, blue, green)')

    data = []
    with open('./input.txt') as inputfile:
        for line in inputfile:
            data.extend(extract_data(line))

    cursor.executemany('INSERT INTO game VALUES (?, ?, ?, ?)', data)
    connection.commit()

    #part_one(connection)
    part_two(connection)

    connection.close()
