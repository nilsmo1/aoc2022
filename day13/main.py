# Day 13, Distress Signal
from typing import List, Any
from itertools import zip_longest

Pair = List[List[Any]]

# Q1
def compare(p1: List[Any], p2: List[Any]) -> str:
    l = lambda e: isinstance(e, list)
    i = lambda e: isinstance(e, int)
    match (l(p1), l(p2)):
        case (True , True ):
            for i in range(min(len(p1), len(p2))):
                local_comp = compare(p1[i], p2[i])
                if local_comp == 'ok':
                    return 'ok'
                elif local_comp == 'nok':
                    return 'nok'
            if len(p1) < len(p2):
                return 'ok'
            elif len(p2) < len(p1):
                return 'nok'
            else: return 'eq'
        case (True , False): return compare( p1 , [p2])
        case (False, True ): return compare([p1],  p2 )
        case (False, False):
            if p1<p2: return 'ok'
            elif p1==p2: return 'eq'
            else: return 'nok'

def get_correct(pairs: List[Pair]) -> int: 
    return sum(c+1 for c, [p1, p2] in enumerate(pairs) if compare(p1, p2)=='ok')

# Q2
def get_correct_order(pairs: List[Pair]) -> int:
    all_packets = [ [[2]], [[6]] ]
    for pair in pairs: 
        all_packets.append(pair[0])
        all_packets.append(pair[1])
    order = all_packets[:2]
    for packet in all_packets:
        for i, (p1, p2) in enumerate(zip(order, order[1:])):
            if compare(packet, p1) == 'ok':
                order.insert(i, packet)
                break
            if compare(p2, packet) == 'ok':
                order.insert(i+2, packet)
                break
            if compare(p1, packet) == 'ok' and compare(packet, p2) == 'ok':
                order.insert(i+1, packet)
                break
    while not all(compare(p, p1) in ('ok', 'eq') and compare(p1, p2) in ('ok', 'eq') for p, p1 in zip(order, order[1:])):
        for i, (p, p1, p2) in enumerate(zip(order, order[1:], order[2:])):
            c, c2 = compare(p, p1), compare(p1,p2)
            if c == 'nok':
                order[i  ] = p1
                order[i+1] = p
                break
            if c2 == 'nok':
                order[i+1] = p2
                order[i+2] = p1
                break
    return (order.index([[2]])+1) * (order.index([[6]])+1)

# Input
def parse_input(file: str) -> List[Pair]:
    with open(file, 'r') as inp:
        return [[eval(line) for line in pair.split('\n')] for pair in inp.read().strip().split('\n\n')] 

if __name__ == '__main__':
    # Sample
    sample_input = parse_input('sample')

    # Tests
    assert get_correct(sample_input)        == 13
    assert get_correct_order(sample_input) == 140
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = get_correct(puzzle_input)
    q2 = get_correct_order(puzzle_input)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
