# Day 7, No Space Left On Device
from typing import List, Dict, Any

# Q1
def add_subdirs(dirs: Dict[str, Any], key: str) -> Dict[str, Any]:
    q = list(dirs[key][0])
    while q:
        d = q.pop()
        subdirs = dirs[d][0]
        for subdir in subdirs: q.append(subdir)
        dirs[key][1]+=dirs[d][1]
    return dirs[key][1]

def finalize(dirs: Dict[str, Any]) -> Dict[str, Any]:
    for d in list(dirs): dirs[d][1] = add_subdirs(dirs, d)
    return dirs

def from_cond(dirs: Dict[str, Any], threshold) -> int:
    return sum(mem[1] for mem in dirs.values() if mem[1] <= threshold) 

# Q2
def del_optimal_dir(dirs: Dict[str, Any]) -> int:
    total = 70_000_000
    root  = dirs['/'][1]
    have  = total - root
    need  = 30_000_000
    min_dir = total
    for d, [_, mem] in dirs.items():
        if mem + have >= need: min_dir = min(min_dir, mem)
    return min_dir
    
# Input
def parse_input(file: str) -> List[str]:
    with open(file, 'r') as inp:
        return [line.strip().split() for line in inp.read().strip().splitlines()]

def parse(trace: List[str]) -> Dict[str, Any]:
    path, dir_trace = {}, []
    abspath = lambda dt: '/'.join(dt)
    for cmd in trace:
        match cmd:
            case ['$', 'ls']: pass
            case ['$', 'cd', '..']:
                dir_trace.pop()
            case ['$', 'cd', d]:
                dir_trace.append(d)
                path[abspath(dir_trace)] = [[], 0]
            case ['dir', name]:
                path[abspath(dir_trace)][0].append(abspath(dir_trace+[name]))
            case [size, name]:
                path[abspath(dir_trace)][1]+=int(size)
    return path

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')
    parsed_sample = parse(sample_input)
    sample_final = finalize(parsed_sample)

    # Tests
    assert from_cond(sample_final, 100_000) == 95437
    assert del_optimal_dir(sample_final)    == 24933642

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')
    parsed_puzzle = parse(puzzle_input)
    puzzle_final = finalize(parsed_puzzle)

    # Results
    q1 = from_cond(puzzle_final, 100_000)
    q2 = del_optimal_dir(puzzle_final)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
