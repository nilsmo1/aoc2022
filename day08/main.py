# Day 8, Treetop Tree House
from typing import List, Tuple

Map = List[List[int]]

# Q1
def side(t: Map, d: Tuple[int, int], row: int, col: int) -> List[int]:
    match d:
        case ( _, 1): return                  t[row][col+1:]
        case ( _,-1): return                  t[row][:col]
        case ( 1, _): return [v[col] for v in t[row+1:]]
        case (-1, _): return [v[col] for v in t[:row]]

def visible(tree_map: Map, row: int, col: int, tree: int) -> bool:
    return any(all(tree > other for other in side(tree_map, d, row, col))
               for d in [(0,1), (0,-1), (1,0), (-1, 0)])

def potentials(tree_map: Map, rs: int, cs: int) -> Map:
    return [(row, col, tree_map[row][col])
             for row in range(1, rs-1) for col in range(1, cs-1)]

def how_many_visible(tree_map: Map) -> int:
    rs, cs = len(tree_map), len(tree_map[0])
    potential = potentials(tree_map, rs, cs)
    return sum(visible(tree_map, r, c, t) for r,c,t in potential) + 2*(rs + cs - 2)

# Q2
def scenic_score(tree_map: Map, row: int, col: int, tree: int) -> int:
    side_scores = {c : 0 for c in range(4)}
    for c, d in enumerate([(0,1), (0,-1), (1,0), (-1,0)]):
        s = side(tree_map, d, row, col)
        for other_tree in (s[::-1] if -1 in d else s):
            side_scores[c] += 1
            if tree <= other_tree: break
    l, r, u, d = side_scores.values()
    return l * r * u * d
            
def highest_scenic_score(tree_map: Map) -> int:
    rs, cs = len(tree_map), len(tree_map[0])
    potential = potentials(tree_map, rs, cs)
    return max(scenic_score(tree_map, r, c, t) for r, c, t in potential)

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
