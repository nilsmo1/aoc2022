# Day 2, Rock Paper Scissors

# Q1
def play(insts):
    # A X Rock
    # B Y Paper
    # C Z Scissors
    wins = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    ties = {'X': 'A', 'Y': 'B', 'Z': 'C'} 
    score = 0
    for a, b in insts:
        if   a == ties[b]: score+=3
        elif a == wins[b]: score+=6
        score+=ord(b)-ord('X')+1
    return score

# Q2
def play_2(insts):
    # X Lose
    # Y Tie
    # Z Win
    moves = 'ABC'
    score = 0
    outcome = lambda c, off: (moves.index(c)+off)%3+1
    for a, b in insts:
        if   b == 'X': score+=  outcome(a, -1)
        elif b == 'Y': score+=3+outcome(a,  0)
        elif b == 'Z': score+=6+outcome(a,  1)
    return score

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return [line.strip().split() for line in inp]

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')
    
    # Tests
    assert play(sample_input)   == 15
    assert play_2(sample_input) == 12 

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')
    
    # Results
    q1 = play(puzzle_input)
    q2 = play_2(puzzle_input)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
