# Day 5, Supply Stacks
from typing import List, Tuple, DefaultDict, NamedTuple
import re
from collections import defaultdict

Init  = DefaultDict[int, List[str]]

class Instruction(NamedTuple):
    quantity : int
    from_idx : int
    to_idx   : int

# Q1
def run(init: Init, insts: List[Instruction]) -> str:
    for inst in insts:
        quan, fr, to = inst
        for q in range(quan):
            init[to].append(init[fr].pop())
    init = sorted(init.items(), key=lambda x: x[0])
    return ''.join([vals[1][-1] for vals in init])

# Q2
def run_keep_order(init: Init, insts: List[Instruction]) -> str:
    for inst in insts:
        quan, fr, to = inst
        buffer = []
        for q in range(quan): buffer = [init[fr].pop()] + buffer
        for e in buffer: init[to].append(e)
    init = sorted(init.items(), key=lambda x: x[0])
    return ''.join([vals[1][-1] for vals in init])

# Input
def parse_input(file: str) -> Tuple[List[str], List[str]]:
    with open(file, 'r') as inp:
        init, insts = inp.read().split('\n\n')
    init = [line for line in init.split('\n')]
    insts = [line.strip() for line in insts.split('\n') if line]
    return (init, insts)

def parse_init(init: List[str]) -> Init:
    cols = defaultdict(list)
    for row in init[:-1]:
        i = 0
        while True:
            check = row[:3]
            if check.strip(): cols[i] = [check.strip()[1]] + cols[i]
            if len(row): row = row[4:]
            else: break
            i+=1
    return cols

def parse_insts(insts: List[str]) -> List[Instruction]:
    rgx = r'move (\d+) from (\d+) to (\d+)'
    parsed = []
    for inst in insts:
        match = re.match(rgx, inst).groups()
        q, fr, to = match
        parsed_inst = Instruction(int(q), int(fr)-1, int(to)-1)
        parsed.append(parsed_inst)
    return parsed


if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')
    sample_init, sample_insts = sample_input
    _sample_init = parse_init(sample_init)
    sample_insts = parse_insts(sample_insts)

    # Tests
    assert run(_sample_init, sample_insts) == 'CMZ'
    assert run_keep_order(parse_init(sample_init), sample_insts) == 'MCD'

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')
    puzzle_init, puzzle_insts = puzzle_input
    _puzzle_init = parse_init(puzzle_init)
    puzzle_insts = parse_insts(puzzle_insts)

    # Results
    q1 = run(_puzzle_init, puzzle_insts)
    q2 = run_keep_order(parse_init(puzzle_init), puzzle_insts)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
