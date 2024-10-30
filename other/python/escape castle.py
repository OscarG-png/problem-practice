#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'escape_castle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER rows
#  2. INTEGER columns
#  3. 2D_INTEGER_ARRAY walls
#  4. INTEGER_ARRAY escape_point
#
from collections import deque
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

class Castle:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[0 for _ in range(columns)] for _ in range(rows)]

    def is_valid_position(self, position):
        return (0 <= position.x < self.rows and 0 <= position.y < self.columns)


class Adventurer:
    def __init__(self, position):
        self.position = position
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def get_possible_moves(self, castle, walls):
        moves = []
        for dx, dy in self.directions:
            new_pos = Position(self.position.x + dx, self.position.y + dy)
            if (castle.is_valid_position(new_pos) and not walls.is_wall(new_pos)):
                moves.append(new_pos)
        return moves

class Walls:
    def __init__(self, wall_positions):
        self.wall_positions = {Position(x, y) for x, y in wall_positions}

    def is_wall(self, position):
        return position in self.wall_positions

def escape_castle(rows, columns, walls, escape_point):
    # Write your code here
    castle = Castle(rows, columns)
    walls = Walls(walls)
    start = Position(0, 0)
    end = Position(escape_point[0], escape_point[1])
    adventurer = Adventurer(start)

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        current_pos, steps = queue.popleft()

        if current_pos == end:
            return [steps]

        adventurer.position = current_pos
        for new_pos in adventurer.get_possible_moves(castle, walls):
            if new_pos not in visited:
                visited.add(new_pos)
                queue.append((new_pos, steps + 1))
    return [-1]
