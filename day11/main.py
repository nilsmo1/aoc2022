# Day 11, Monkey in the Middle
from typing import List, Deque, Tuple, Union
from collections import deque, defaultdict
from dataclasses import dataclass
from copy import deepcopy
from math import gcd

@dataclass
class Monkey:
    idx: int
    items: Deque[int]
    op: Tuple[str, Union[str, int]]
    test: int
    if_true: int
    if_false: int
    inspected: int = 0
    
    def do_op(self, val: int) -> int:
        match self.op:
            case ['*', 'old']: return val*val
            case ['+', 'old']: return val+val
            case ['*',   i  ]: return val*i
            case ['+',   i  ]: return val+i

    def do_turn(self) -> List[Tuple[int, int]]: 
        _passes = []
        while self.items:
            self.inspected+=1
            item = self.items.popleft()
            _new = self.do_op(item)
            _new //= 3
            _passes.append((_new, self.if_true if _new % self.test == 0 else self.if_false))
        return _passes

# Q1
def do_round(ms: List[Monkey]) -> List[Monkey]:
    for m in ms:
        _passes = m.do_turn()
        for _new, _pass in _passes:
            ms[_pass].items.append(_new)
    return ms

def do_rounds(ms: List[Monkey], rounds: int=20) -> int:
    for i in range(rounds):
        ms = do_round(ms)
    m1, m2 = sorted([m.inspected for m in ms], reverse=True)[:2]
    return m1*m2

# Q2
def do_rounds_better(ms: List[Monkey], rounds: int=10000) -> int:
    inspected = defaultdict(int)
    lcm = 1
    for m in ms: lcm *= (lcm*m.test)//gcd(lcm, m.test)
    for round in range(1,rounds+1):
        for mid, m in enumerate(ms):
            while m.items:
                inspected[mid]+=1
                item = m.items.popleft()
                n = m.do_op(item)%lcm
                if n % m.test == 0: ms[m.if_true].items.append(n)
                else: ms[m.if_false].items.append(n)
    m1, m2 = sorted(inspected.values(), reverse=True)[:2]
    return m1*m2

# Input
def parse_input(file: str) -> List[Monkey]:
    ms = []
    with open(file, 'r') as inp:
        for monkey in inp.read().strip().split('\n\n'):
            idx, items, op, test, if_true, if_false = [r.strip() for r in monkey.splitlines()]
            idx = int(idx.split()[1][:-1])
            items = deque([int(x) for x in items[len('Starting items: '):].split(', ')])
            operands = op.split()[1::2]
            oper = ('+' if '+' in op else '*', 'old' if operands[-1] == 'old' else int(operands[-1]))
            test = int(test.split()[-1])
            if_true = int(if_true.split()[-1])
            if_false = int(if_false.split()[-1])
            ms.append(Monkey(idx, items, oper, test, if_true, if_false))
        return ms

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')
    sample_cpy = deepcopy(sample_input)

    # Tests
    assert do_rounds(sample_cpy) == 10605
    assert do_rounds_better(sample_input) == 2713310158
    
    # Puzzle input
    puzzle_input = parse_input('puzzle-input')
    puzzle_cpy = deepcopy(puzzle_input)

    # Results
    q1 = do_rounds(puzzle_cpy)
    q2 = do_rounds_better(puzzle_input)

    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
