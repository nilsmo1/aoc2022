# Day 8, Treetop Tree House
from typing import List, Tuple, Callable

Map = List[List[int]]
Potential = List[Tuple[int, int, int]]

# Q1
def init(t_map: Map) -> Tuple[int, int, Potential]:
    rs, cs = len(t_map), len(t_map[0])
    return rs, cs, potentials(t_map, rs)

def potentials(t_map: Map, rs: int) -> Potential:
    return [(row, col+1, t) for row in range(1, rs-1) for col, t in enumerate(t_map[row][1:-1])]

def side(t_map: Map, rs: int, cs: int, row: int, col: int, row_flag: int, d: int) -> List[int]:
    return [v[col] for v in t_map[0 if d else row+1 : row if d else rs]] if row_flag else \
            t_map[row][0 if d else col+1 : col if d else cs]

def visible(t_map: Map, row: int, col: int, tree: int, rs: int, cs: int) -> bool:
    return any(all(tree > other for other in side(t_map, rs, cs, row, col, rf, d))
               for rf, d in [(1,1), (0,1), (1,0), (0,0)])

def answer(t_map: Map, func: Callable[[Map, int, int, int, int, int], int], p1: bool=False) -> int:
    rs, cs, potential = init(t_map)
    vs = [func(t_map, r, c, t, rs, cs) for r, c, t in potential]
    return sum(vs) + 2*(rs + cs - 2) if p1 else max(vs)

# Q2
def scenic_score(t_map: Map, row: int, col: int, tree: int, rs: int, cs: int) -> int:
    side_scores = {c : 0 for c in range(4)}
    for c, (rf, d) in enumerate([(1,1), (0,1), (1,0), (0,0)]):
        s = side(t_map, rs, cs, row, col, rf, d)
        for other_tree in (s[::-1] if d else s):
            side_scores[c] += 1
            if tree <= other_tree: break
    l, r, u, d = side_scores.values()
    return l * r * u * d

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return [[int(x) for x in line] for line in inp.read().strip().splitlines()]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    assert answer(sample_input, visible, True) == 21
    assert answer(sample_input, scenic_score)  == 8
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = answer(puzzle_input, visible, True)
    q2 = answer(puzzle_input, scenic_score)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
