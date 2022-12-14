# Day 14, Regolith Reservoir
from typing import List, Tuple
from collections import defaultdict

# Q1
def all_obs(obstacles: List[List[Tuple[int, int]]]) -> List[Tuple[int, int]]:
    all_obstacles = []
    for line in obstacles:
        sx, sy = line[0]
        for nx, ny in line[1:]:
            if nx == sx:
                for y in range(min(sy, ny), max(sy, ny)+1):
                    all_obstacles.append((sx, y))
            else:
                for x in range(min(sx, nx), max(sx, nx)+1):
                    all_obstacles.append((x, sy))
            sx, sy = nx, ny
    return all_obstacles

def move(sx, sy, stones):
    if (sx, sy+1) not in stones:
        return sx, sy+1
    if (sx-1, sy+1) not in stones:
        return sx-1, sy+1
    if (sx+1, sy+1) not in stones:
        return sx+1, sy+1
    return None

def drop_sand(obstacles: List[List[Tuple[int, int]]]) -> int:
    srcx, srcy = src = 500, 0
    units = 0
    all_stones = all_obs(obstacles)
    max_y = max(y for x, y in all_stones)
    min_x = min(x for x, y in all_stones)
    max_x = max(x for x, y in all_stones)
    while True:
        sx, sy = src
        while move(sx, sy, all_stones) is not None:
            sx, sy = move(sx, sy, all_stones)
            if sy>max_y or not min_x <= sx <= max_x: return units
        units+=1
        all_stones.append((sx, sy))
    return units   

# Q2
def move_2(sx, sy, stones):
    if not stones[(sx, sy+1)]:
        return sx, sy+1
    if not stones[(sx-1, sy+1)]:
        return sx-1, sy+1
    if not stones[(sx+1, sy+1)]:
        return sx+1, sy+1
    return None

def drop_sand_until_done(obstacles: List[List[Tuple[int, int]]]) -> int:
    srcx, srcy = src = 500, 0
    units = 0
    stones = all_obs(obstacles)
    all_stones = defaultdict(bool)
    for (x,y) in stones: all_stones[(x,y)] = True
    max_y = max(y for x, y in all_stones)
    min_x = min(x for x, y in all_stones)
    max_x = max(x for x, y in all_stones)
    floor = max_y+2
    while (500, 0) not in all_stones:
        sx, sy = src
        while True:
            m = move_2(sx, sy, all_stones)
            if m is None: break
            sx, sy = m
            if sy == floor-1: break
        units+=1
        all_stones[(sx,sy)] = True
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
    assert drop_sand(sample_input)            == 24
    assert drop_sand_until_done(sample_input) == 93
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = drop_sand(puzzle_input)
    q2 = drop_sand_until_done(puzzle_input)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
