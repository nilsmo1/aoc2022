# Day 6, Tuning Trouble
from typing import List, Union

# Q1 & Q2
def report_first_marker(signal: str, packet: bool) -> int:
    for s, _ in enumerate(signal):
        if     packet and len(set(signal[s:s+4]))  == 4 : return s+4
        if not packet and len(set(signal[s:s+14])) == 14: return s+14
    assert False

# Input
def parse_input(file: str) -> Union[List[str], str]:
    with open(file, 'r') as inp:
        output = inp.read().strip().splitlines()
    if len(output) == 1: return output.pop()
    return [line.strip() for line in output]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    sample_asserts_p1 = [7 , 5 , 6 , 10, 11]
    sample_asserts_p2 = [19, 23, 23, 29, 26]
    for s, sa_p1, sa_p2 in zip(sample_input, sample_asserts_p1, sample_asserts_p2):
        assert report_first_marker(s, True)  == sa_p1
        assert report_first_marker(s, False) == sa_p2

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = report_first_marker(puzzle_input, True)
    q2 = report_first_marker(puzzle_input, False)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
