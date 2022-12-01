# Day 01, Calorie Counting

# Q1
def most_cals(lines):
    m, current = 0, 0
    for line in lines:
        if line != '\n': 
            line = int(line.strip())
            current+=line
        else:
            m = max(current, m)
            current = 0
    return m

# Q2
def three_most_cals(lines):
    cals, current = [], 0
    for line in lines:
        if line != '\n': 
            line = int(line.strip())
            current+=line
        else:
            cals.append(current)
            current = 0
    cals.sort()
    return sum(cals[-i] for i in range(1,4))


if __name__ == '__main__':
    # Samples
    with open('sample', 'r') as sample:
        sample_input = [line for line in sample]
    
    # Tests
    
    # Puzzle input
    with open('puzzle-input', 'r') as RAW:
        formatted = [line for line in RAW] 
    
    # Results
    q1 = most_cals(formatted)
    q2 = three_most_cals(formatted)
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
