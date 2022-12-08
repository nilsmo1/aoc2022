# Day 8, Treetop Tree House
from typing import List, Tuple

Map = List[List[int]]

# Q1
def init(tree_map: Map) -> Tuple[int, int, Map]:
    rs, cs = len(tree_map), len(tree_map[0])
    return rs, cs, potentials(tree_map, rs, cs)

def potentials(tree_map: Map, rs: int, cs: int) -> Map:
    return [(row, col, tree_map[row][col]) for row in range(1, rs-1) for col in range(1, cs-1)]

def side(t: Map, rs: int, cs: int, row: int, col: int, row_flag: int, d: int) -> List[int]:
    if row_flag: return [v[col] for v in t[0 if d else row+1 : row if d else rs]]
    return t[row][0 if d else col+1 : col if d else cs]

def visible(tree_map: Map, row: int, col: int, tree: int, rs: int, cs: int) -> bool:
    return any(all(tree > other for other in side(tree_map, rs, cs, row, col, rf, d))
               for rf, d in [(1,1), (0,1), (1,0), (0,0)])

def how_many_visible(tree_map: Map) -> int:
    rs, cs, potential = init(tree_map) 
    return sum(visible(tree_map, r, c, t, rs, cs) for r, c, t in potential) + 2*(rs + cs - 2)

# Q2
def scenic_score(tree_map: Map, row: int, col: int, tree: int, rs: int, cs: int) -> int:
    side_scores = {c : 0 for c in range(4)}
    for c, (rf, d) in enumerate([(1,1), (0,1), (1,0), (0,0)]):
        s = side(tree_map, rs, cs, row, col, rf, d)
        for other_tree in (s[::-1] if d else s):
            side_scores[c] += 1
            if tree <= other_tree: break
    l, r, u, d = side_scores.values()
    return l * r * u * d
            
def highest_scenic_score(tree_map: Map) -> int:
    rs, cs, potential = init(tree_map) 
    return max(scenic_score(tree_map, r, c, t, rs, cs) for r, c, t in potential)

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return [[int(x) for x in line] for line in inp.read().strip().splitlines()]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    assert how_many_visible(sample_input)     == 21
    assert highest_scenic_score(sample_input) == 8
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = how_many_visible(puzzle_input)
    q2 = highest_scenic_score(puzzle_input)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
