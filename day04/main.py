# Day 4, Camp Cleanup 
from typing import NamedTuple, List, Callable

class Sections(NamedTuple):
    low  : int
    high : int

class Pair(NamedTuple):
    first  : Sections 
    second : Sections 

def count_criteria(ps: List[Pair], full: bool) -> int:
    return sum(overlap(p, full) for p in ps)

# Q1 & Q2
def overlap(p: Pair, full: bool) -> bool:
    s1, s2 = p.first, p.second
    l1, l2 = s1.low , s2.low
    h1, h2 = s1.high, s2.high
    if full: return (l1 <= l2 and h1 >= h2 or 
                     l1 >= l2 and h1 <= h2)
    return (l1<=l2<=h1 or
            l1<=h2<=h1 or
            l2<=l1<=h2 or
            l2<=h1<=h2)

# Input
def parse_input(file: str) -> List[Pair]:
    spl = lambda l, i: list(map(int, l.split('-')[i]))
    parsed = []
    with open(file, 'r') as inp:
        for line in inp.read().strip().split('\n'):
            p1, p2 = line.split(',')
            l1, h1 = map(int, p1.split('-'))
            l2, h2 = map(int, p2.split('-'))
            sec1 = Sections(l1, h1)
            sec2 = Sections(l2, h2)
            parsed.append(Pair(sec1, sec2))
    return parsed

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    assert count_criteria(sample_input, True)  == 2
    assert count_criteria(sample_input, False) == 4
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = count_criteria(puzzle_input, True)
    q2 = count_criteria(puzzle_input, False)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
