# Day 01, Calorie Counting

# Q1
def most_cals(lines):
    return max(sum(line) for line in lines)

# Q2
def three_most_cals(lines):
    lines = [sum(line) for line in lines]
    return sum(sorted(lines)[-3:])


# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return [[int(x) for x in line.split('\n')] for line in inp.read().strip().split('\n\n')]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    assert most_cals(sample_input)       == 24000
    assert three_most_cals(sample_input) == 45000

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = most_cals(puzzle_input)
    q2 = three_most_cals(puzzle_input)
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
