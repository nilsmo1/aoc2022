# Day 14, Regolith Reservoir
from typing import List, Tuple, DefaultDict
from collections import defaultdict

# Q1 & Q2
def all_obs(obstacles: List[List[Tuple[int, int]]]) -> DefaultDict[Tuple[int, int], bool]:
    all_obstacles = defaultdict(bool)
    for line in obstacles:
        sx, sy = line[0]
        for nx, ny in line[1:]:
            if nx == sx:
                for y in range(min(sy, ny), max(sy, ny)+1):
                    all_obstacles[(sx, y)] = True
            else:
                for x in range(min(sx, nx), max(sx, nx)+1):
                    all_obstacles[(x, sy)] = True
            sx, sy = nx, ny
    return all_obstacles

def move(sx: int, sy: int, stones: DefaultDict[Tuple[int, int], bool]) -> Tuple[int, int]:
    if not stones[(sx  , sy+1)]: return sx  , sy+1
    if not stones[(sx-1, sy+1)]: return sx-1, sy+1
    if not stones[(sx+1, sy+1)]: return sx+1, sy+1
    return None

def drop_sand(obstacles: List[List[Tuple[int, int]]], floor: bool) -> int:
    srcx, srcy, units = 500, 0, 0
    all_stones = all_obs(obstacles)
    max_y = max(y for x, y in all_stones)
    while not all_stones[(srcx, srcy)]:
        sx, sy = srcx, srcy
        while True:
            m = move(sx, sy, all_stones)
            if m is None: break
            sx, sy = m
            if   sy >= max_y   and not floor: return units
            elif sy == max_y+1 and     floor: break
        all_stones[(sx, sy)], units = True, units+1
    return units   

# Input
def parse_input(file: str) -> List[List[Tuple[int, int]]]:
    ret = []
    with open(file, 'r') as inp:
        for line in inp.read().strip().splitlines():
            ps = []
            for c in line.strip().split(' -> '):
                x, y = c.split(',')
                ps.append((int(x),int(y)))
            ret.append(ps)
    return ret

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    assert drop_sand(sample_input, False) == 24 
    assert drop_sand(sample_input, True ) == 93 
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = drop_sand(puzzle_input, False)
    q2 = drop_sand(puzzle_input, True )

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
