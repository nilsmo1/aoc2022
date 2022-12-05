# Day 5, Supply Stacks
from typing import List, Tuple, DefaultDict, NamedTuple
from collections import defaultdict

Init = DefaultDict[int, List[str]]

class Instruction(NamedTuple):
    quantity : int
    from_idx : int
    to_idx   : int

# Q1 & Q2
def run(init: Init, insts: List[Instruction], keep_order: bool) -> str:
    for quan, fr, to in insts:
        if keep_order: init[to]+=[init[fr].pop() for _ in range(quan)][::-1]
        else: init[to]+=[init[fr].pop() for _ in range(quan)]
    return ''.join([v[1][-1] for v in sorted(init.items(), key=lambda x: x[0])])

# Input
def parse_input(file: str) -> Tuple[List[str], List[str]]:
    with open(file, 'r') as inp:
        init, insts = inp.read().split('\n\n')
    return [line for line in init.split('\n')], [line.strip() for line in insts.split('\n') if line]

def parse_init(init: List[str]) -> Init:
    cols = defaultdict(list)
    for row in init[:-1]:
        for i in range((len(row)+1)//4):
            check = row[4*i:4*(i+1)].strip()
            if check: cols[i] = [check[1]] + cols[i]
    return cols

def parse_insts(insts: List[str]) -> List[Instruction]:
    return [Instruction(int(q), int(fr)-1, int(to)-1) for q, fr, to in [inst.split()[1::2] for inst in insts]]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')
    sample_init, sample_insts = sample_input

    # Tests
    assert run(parse_init(sample_init), parse_insts(sample_insts), False) == 'CMZ'
    assert run(parse_init(sample_init), parse_insts(sample_insts), True)  == 'MCD'

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')
    puzzle_init, puzzle_insts = puzzle_input

    # Results
    q1 = run(parse_init(puzzle_init), parse_insts(puzzle_insts), False)
    q2 = run(parse_init(puzzle_init), parse_insts(puzzle_insts), True)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
