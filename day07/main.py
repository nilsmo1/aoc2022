# Day 7, No Space Left On Device
from typing import List, Dict, Any

# Q1
#{
# '/': [['a', 'd'], 23352670], 
# 'a': [['e'], 94269], 
# 'e': [[], 584], 
# 'd': [[], 24933642]
#}

def add_subdirs(dirs: Dict[str, Any], key: str) -> Dict[str, Any]:
    q = list(dirs[key][0])
    print(q)
    while q:
        d = q.pop()
        subdirs = dirs[d][0]
        for subdir in subdirs:
            q.append(subdir)
        dirs[key][1]+=dirs[d][1]
    return dirs[key][1]

def finalize(dirs: Dict[str, Any]) -> Dict[str, Any]:
    cp = list(dirs)
    for d in cp:
        print(d, f'before finalize: {dirs[d][1]}')
        dirs[d][1] = add_subdirs(dirs, d)
        print(d, f'after finalize: {dirs[d][1]}')
    #print(dirs)
    return dirs

def from_cond(dirs: Dict[str, Any], threshold) -> int:
    #for mem in dirs.values(): print(mem)
    return sum(mem[1] for mem in dirs.values() if mem[1] <= threshold) 

# Q2

# Input
def parse_input(file: str) -> List[str]:
    with open(file, 'r') as inp:
        return [line.strip().split() for line in inp.read().strip().splitlines()]

def parse(trace: List[str]) -> Dict[str, Any]:
    path = {}
    dir_trace = []
    for cmd in trace:
        match cmd:
            case ['$', 'ls']: pass
            case ['$', 'cd', '..']:
                dir_trace.pop()
            case ['$', 'cd', d]:
                dir_trace.append(d)
                path[d] = [[], 0]
            case ['dir', name]:
                path[dir_trace[-1]][0].append(name)
            case [size, name]:
                path[dir_trace[-1]][1]+=int(size)
    return path

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')
    parsed_sample = parse(sample_input)
    sample_final = finalize(parsed_sample)

    # Tests
    assert from_cond(sample_final, 100_000) == 95437

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')
    parsed_puzzle = parse(puzzle_input)
    puzzle_final = finalize(parsed_puzzle)

    # Results
    q1 = from_cond(puzzle_final, 100_000)

    print(f'Q1: {q1}')
    print(f'Q2: ')
