# Day 15, Beacon Exclusion Zone
from typing import List, Tuple, Set, DefaultDict
from collections import deque, defaultdict

Sensor = Tuple[int, int]
Beacon = Tuple[int, int]
Coord  = Tuple[int, int]
Pair   = Tuple[Sensor, Beacon]
Pairs  = List[Pair]

# Q1
def flood(sensor: Sensor, beacons: Set[Beacon], founds: Set[Beacon], row: int) -> DefaultDict[int, int]:
    nbs = lambda x, y: [(x+dx, y+dy) for dx, dy in [(-1,0), (0,1), (1, 0), (0, -1)]]
    sx, sy = sensor
    found = None
    ret = 0
    seen = set()
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        ns = nbs(x,y)
        for n in ns:
            if n in seen: continue
            q.append(n)
            seen.add(n)
            if n in beacons: 
                ret -= 1 if n not in founds and n[1] == row else 0
                found = n
            else: ret += 1 if n[1] == row else 0
        if found: break
    return ret, found

# Idea: create outer box
"""
---------------
|      .      |
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
# big box width = 2*dx + 1
# big box height = 2*(dy+dx) + 1
# marked at 10 = 
# 0 if dto10 is outside of square
# 1 + 2*dto10 otherwise


def find_impossible(ps: Pairs, row: int) -> int:
    sensors, beacons = set(p[0] for p in ps), set(p[1] for p in ps)
    min_sx , max_sx  = min(s[0] for s in sensors), max(s[0] for s in sensors) 
    # min_sy , max_sy  = min(s[1] for s in sensors), max(s[1] for s in sensors) 
    min_bx , max_bx  = min(b[0] for b in beacons), max(b[0] for b in beacons) 
    # min_by , max_by  = min(b[1] for b in beacons), max(b[1] for b in beacons) 
    min_x  , max_x   = min(min_sx, min_bx)       , max(max_sx, max_bx)
    # min_y  , max_y   = min(min_sy, min_by)       , max(max_sy, max_by)
    beacons_at_row = sum(1 for x, y in beacons if y == row)
    imps = 0
    founds = set()
    for s in sensors: 
        i, f = flood(s, beacons, founds, row)
        imps += i
        founds.add(f)
    return imps

# Q2

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
    assert find_impossible(sample_input, 10) == 26
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = find_impossible(puzzle_input, 2_000_000)

    print(f'Q1: {q1}')
    print(f'Q2: ')
