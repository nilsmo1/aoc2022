# Day 01, Calorie Counting

# Q1
def most_cals(lines):
    return max(sum(line) for line in lines)

# Q2
def three_most_cals(lines):
    lines = [sum(line) for line in lines]
    return sum(sorted(lines)[-3:])


if __name__ == '__main__':
    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [[int(x) for x in line.split("\n")] for line in RAW.read().strip().split("\n\n")] 

    # Results
    q1 = most_cals(formatted)
    q2 = three_most_cals(formatted)
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
