import itertools


def star1(spreadsheet):
    return sum(max(r)-min(r) for r in spreadsheet)


def star2(spreadsheet):
    return sum(a//b for r in spreadsheet for a,b in itertools.permutations(r,2) if a%b==0)


if __name__=='__main__':
    import sys
    problem_input = [[int(v) for v in l.strip().split('\t')] for l in sys.stdin.readlines()]
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
