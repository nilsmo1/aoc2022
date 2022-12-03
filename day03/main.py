# Day 3, Rucksack Reorganization

# Q1
def char_to_val(char):
    if char.islower(): return ord(char) - ord('a') + 1
    return ord(char) - ord('A') + 27

def common(h1, h2):
    return char_to_val(*set(h1).intersection(set(h2)))

def sum_commons(lines):
    return sum(common(*line) for line in lines)

# Q2
def unparse(h):
    return set(''.join(h[0] + h[1]))

def common_three(e1, e2, e3):
    return e1.intersection(e2).intersection(e3)

def elf_badges(lines):
    total = 0
    for i in range(len(lines)//3):
        elves = [lines[3*i], lines[3*i+1], lines[3*i+2]]
        es = map(unparse, elves)
        total += char_to_val(*common_three(*es))
    return total

# Input
def parse_input(file):
    spl = lambda s: (s[: len(s)//2 ], s[ len(s)//2 :])
    with open(file, 'r') as inp:
        return [spl(line) for line in inp.read().split('\n') if line]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    assert sum_commons(sample_input) == 157
    assert elf_badges(sample_input)  == 70
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = sum_commons(puzzle_input)
    q2 = elf_badges(puzzle_input)
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
