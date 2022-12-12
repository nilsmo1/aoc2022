# Day 12, Hill Climbing Algorithm
from typing import List, Tuple
from collections import deque
from math import inf

Point = Tuple[int, int]

# Q1
def allowed(grid: List[str], p: Point, oth: Point) -> bool:
    (r, c), (rr, cc) = p, oth
    if grid[r ][c ] == 'S': return True
    if grid[rr][cc] == 'E': return ord('z') <= ord(grid[r][c])+1
    return ord(grid[rr][cc]) <= ord(grid[r][c])+1

def neighbours(grid: List[str], r: int, c: int) -> List[Point]:
    return [(r+rr, c+cc) for (rr, cc) in [(-1,0), (0,1), (1,0), (0,-1)]
            if 0 <= r+rr < len(grid) and 0 <= c+cc < len(grid[0]) and allowed(grid, (r, c), (r+rr, c+cc))]

def get_starting(grid: List[str], startchar: str) -> List[Point]:
    return [(r,c) for r,row in enumerate(grid) for c, char in enumerate(grid[r]) if char == startchar]

def traverse(grid: List[str], s: Point) -> int:
    q = deque([(s,0)])
    seen = set()
    while q:
        p, steps = q.popleft()
        if p in seen: continue
        seen.add(p)
        r, c = p
        if grid[r][c] == 'E': return steps
        for n in neighbours(grid, r, c):
            q.append((n, steps+1))
    return inf

# Q2
def min_steps(grid: List[str], ss: str) -> int:
    return min(traverse(grid, s) for s in ss)

# Input
def parse_input(file: str) -> List[str]:
    with open(file, 'r') as inp: return inp.read().splitlines()

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')
    sample_s = get_starting(sample_input, 'S').pop()
    sample_a = get_starting(sample_input, 'a')

    # Tests
    assert traverse(sample_input , sample_s) == 31
    assert min_steps(sample_input, sample_a) == 29
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')
    puzzle_s = get_starting(puzzle_input, 'S').pop()
    puzzle_a = get_starting(puzzle_input, 'a')

    # Results
    q1 = traverse(puzzle_input , puzzle_s)
    q2 = min_steps(puzzle_input, puzzle_a)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
