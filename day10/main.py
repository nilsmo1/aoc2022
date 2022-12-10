# Day 10, Cathode-Ray Tube
from typing import List, Union, Dict

Instruction = Union[str, List[str]]

# Q1 & Q2
def CPU_CRT(instructions: List[Instruction], CRT_flag: bool) -> Dict[int, int]:
    strengths, X = {20+40*i: 0 for i in range(6)}, 1
    inc_at_cycle, off, CRT = {}, 0, ''
    for c, inst in enumerate(instructions, start=1):
        match inst:
            case  'noop': pass
            case ['addx', arg]: 
                inc_at_cycle[c+off+1] = int(arg)
                off += 1
    for cycle in range(1, max(inc_at_cycle)+1):
        if (cycle-1) % 40 == 0 and CRT_flag: print(' '.join(list(CRT))); CRT = ''
        if CRT_flag: CRT += '#' if abs((cycle-1) % 40 - X) <= 1 else ' '
        if cycle in strengths: strengths[cycle] = cycle * X
        X += inc_at_cycle.get(cycle, 0)
    if CRT_flag: print(' '.join(list(CRT))+'\n')
    return strengths

def sum_signals(instructions: List[Instruction], CRT_flag: bool) -> int:
    return sum(CPU_CRT(instructions, CRT_flag).values())

# Input
def parse_input(file: str) -> List[Instruction]:
    with open(file, 'r') as inp:
        return [line if line == 'noop' else line.split() for line in inp.read().splitlines()]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    assert sum_signals(sample_input, False) == 13140
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = sum_signals(puzzle_input, True)

    print(f'Q1: {q1}')
