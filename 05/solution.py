def star1(instructions):
    position = 0
    jumps = 0
    while 0<=position<len(instructions):
        offset = instructions[position]
        instructions[position] += 1
        position += offset
        jumps += 1
    return jumps


def star2(instructions):
    position = 0
    jumps = 0
    while 0<=position<len(instructions):
        offset = instructions[position]
        instructions[position] += 1 if offset<3 else -1
        position += offset
        jumps += 1
    return jumps


if __name__=='__main__':
    import sys
    problem_input = [int(l) for l in sys.stdin.readlines()]
    print(f'*1: {star1(problem_input.copy())}')
    print(f'*2: {star2(problem_input.copy())}')
