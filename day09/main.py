# Day 9, Rope Bridge
from typing import List, Tuple

# Q1 & Q2
def move_to(ny: int, nx: int, cy: int, cx: int) -> Tuple[int, int]:
    if   nx == cx: return (cy+1, cx) if ny > cy else (cy-1, cx)
    elif ny == cy: return (cy, cx+1) if nx > cx else (cy, cx-1)
    if ny > cy: return (cy+1, cx+1) if nx > cx else (cy+1, cx-1)
    if ny < cy: return (cy-1, cx+1) if nx > cx else (cy-1, cx-1)

def move_rope(moves: List[Tuple[str, int]], tails: int) -> int:
    hy, hx = 0,0
    ps, tcs = [(hy, hx) for _ in range(tails)], {(hy, hx)}
    for d, s in moves:
        for _ in range(s):
            py, px = hy, hx
            if   d == 'R': hx+=1
            elif d == 'L': hx-=1
            elif d == 'D': hy+=1
            elif d == 'U': hy-=1
            ny, nx = hy, hx
            for i, (y, x) in enumerate(ps):
                ty, tx = y, x
                neighbour = (y, x) in [(ny+dy, nx+dx) for dy in [-1,0,1] for dx in [-1,0,1]]
                if neighbour: pass 
                elif y != ny or x!= nx: y, x = move_to(ny, nx, y, x)
                else: y, x = py, px
                py, px, ny, nx, ps[i] = ty, tx, y, x, (y, x)
                if i == len(ps)-1: tcs.add((y,x))
    return len(tcs)

# Input
def parse_input(file: str) -> List[Tuple[str, int]]:
    with open(file, 'r') as inp:
        return [(d,int(s)) for d, s in [line.split() for line in inp.read().strip().splitlines()]]

if __name__ == '__main__':
    # Samples
    sample1_input = parse_input('sample1')
    sample2_input = parse_input('sample2')

    # Tests
    assert move_rope(sample1_input, 1) == 13
    assert move_rope(sample1_input, 9) == 1
    assert move_rope(sample2_input, 9) == 36
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = move_rope(puzzle_input, 1)
    q2 = move_rope(puzzle_input, 9)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
