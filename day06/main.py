# Day 6, Tuning Trouble
from typing import List, Union

# Q1 & Q2
def report_first_marker(signal: str, size: int) -> int:
    for s, _ in enumerate(signal):
        if len(set(signal[s:s+size])) == size: return s+size
    assert False, f"unreachable, signal: {signal}, size: {size}"

# Input
def parse_input(file: str) -> Union[List[str], str]:
    with open(file, 'r') as inp:
        output = inp.read().strip().splitlines()
    return output.pop() if len(output) == 1 else [line.strip() for line in output]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    sample_asserts = [(7,19), (5,23), (6,23), (10,29), (11,26)]
    assert all(report_first_marker(s, 4) == sa_p1 and report_first_marker(s, 14) == sa_p2 for
               s, (sa_p1, sa_p2) in zip(sample_input, sample_asserts))

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = report_first_marker(puzzle_input,  4)
    q2 = report_first_marker(puzzle_input, 14)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
