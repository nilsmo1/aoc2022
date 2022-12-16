# Day 15, Beacon Exclusion Zone
from typing import List, Tuple, Set, DefaultDict
from collections import deque, defaultdict

Sensor = Tuple[int, int]
Beacon = Tuple[int, int]
Coord  = Tuple[int, int]
Pair   = Tuple[Sensor, Beacon]
Pairs  = List[Pair]

# Q1
# Idea: create outer box
"""
---------------
|      .      | 10
|     ...     |
|    .....    | 
|   .......   |
|  .........  |
| ........... |
|......S......|
| ........... |
|  B........  |
|   .......   |
|    .....    |
|     ...     |
|      .      |
---------------
"""
# in this example:
# marked = area of big box - unmarked squares
# marked = area of big box - 2 * 6*6 / 2 = 6*6
# dx = 4
# dy = 2
# big box width = 2*(dy+dx) + 1
# big box height = 2*(dy+dx) + 1
# marked at 10 = 
# 0 if dto10 is outside of square
# 1 + 2*dto10 otherwise
def impossible_ids(p: Pair, seen: Set[int], row: int) -> None:
    (sx, sy), (bx, by) = p
    d = abs(sx-bx) + abs(sy-by)
    boxtop, boxbot, boxwidth = sy-d, sy+d, 2*d + 1
    if not boxtop < row < boxbot: return
    dtorow = abs(sy-row)
    atrow = boxwidth - 2*dtorow 
    seen.add(sx)
    for x in range(1,(atrow+1)//2):
        seen.add(sx-x)
        seen.add(sx+x)

def impossibles(ps: Pairs, row: int) -> Tuple[Set[int], int]:
    beacons = set(p[1] for p in ps)
    seen = set()
    for p in ps: impossible_ids(p, seen, row)
    beacons_at_row = sum(1 for _, y in beacons if y == row)
    return seen, len(seen) - beacons_at_row

# Q2
def possible_ids(p: Pair, seen: Set[Coord], row: int) -> None:
    (sx, sy), (bx, by) = p
    d = abs(sx-bx) + abs(sy-by)
    boxtop, boxbot, boxwidth = sy-d, sy+d, 2*d + 1
    if not boxtop < row < boxbot: return
    dtorow = abs(sy-row)
    atrow = boxwidth - 2*dtorow 
    seen.discard((sx, row))
    for x in range(1,(atrow+1)//2):
        seen.discard((sx-x, row))
        seen.discard((sx+x, row))

def possibles(ps: Pairs, seen: Set[Coord], row: int, low: int, high: int) -> None:
    for p in ps: possible_ids(p, seen, row)

def try2(ps: Pairs, low: int, high: int) -> int:
    fresh = {(x,y) for y in range(low, high+1) for x in range(low, high+1)}
    for y in range(low, high+1): possibles(ps, fresh, y, low, high)
    assert len(fresh) == 1
    bx, by = fresh.pop()
    return bx*4_000_000 + by

def tuning_frequency(ps: Pairs, low: int, high: int) -> int:
    seen = {}
    fresh = {(x,y) for y in range(low, high+1) for x in range(low, high+1)}
    for y in range(low, high+1):
        seen[y], _ = impossibles(ps, y)
    for y, _set in seen.items():
        for x in _set:
            if not low <= x <= high: continue
            fresh.remove((x, y))
    assert len(fresh) == 1
    bx, by = fresh.pop()
    return bx*4_000_000 + by



# Input
def parse_input(file: str) -> Pairs:
    ret = []
    with open(file, 'r') as inp:
        for line in inp.read().strip().splitlines():
            split = line.split()
            sx, sy, bx, by = [split[i][2:] for i in [2, 3, 8, 9]]
            sx, sy, bx, by = int(sx[:-1]), int(sy[:-1]), int(bx[:-1]), int(by)
            ret.append(((sx, sy), (bx, by)))
    return ret

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    #assert impossibles(sample_input, 10)[1] == 26
    #assert tuning_frequency(sample_input, 0, 20) == 56_000_011
    assert try2(sample_input, 0, 20) == 56_000_011
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    #q1 = impossibles(puzzle_input, 2_000_000)[1]
    # q2: no smaller than 0 and no larger than 4_000_000
    q2 = try2(puzzle_input, 0, 4_000_000)

    # print(f'Q1: {q1}')
    print(f'Q2: {q2}')
