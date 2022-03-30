import itertools


def redistribute_banks(banks):
    blocks = max(banks)
    index = banks.index(blocks)
    banks[index] = 0
    while blocks:
        index = (index+1)%len(banks)
        banks[index] += 1
        blocks -= 1
    return banks


def star(banks):
    banks = banks.copy()
    seen = {tuple(banks):0}
    for i in itertools.count(1):
        banks = redistribute_banks(banks)
        t = tuple(banks)
        if t in seen:
            return i,i-seen[t]
        else:
            seen[t] = i
    raise Exception('You should not be here')


def star1(banks):
    return star(banks)[0]


def star2(banks):
    return star(banks)[1]


if __name__=='__main__':
    import sys
    problem_input = [int(t) for t in sys.stdin.readline().split('\t')]
    print(f'*1: {star1(problem_input.copy())}')
    print(f'*2: {star2(problem_input.copy())}')
