def star1(string):
    digits = [int(c) for c in string]
    return sum(a for a,b in zip(digits, digits[1:]+digits[:1]) if a==b)

def star2(string):
    digits = [int(c) for c in string]
    return sum(a for a,b in zip(digits, digits[len(digits)//2:]+digits[:len(digits)//2]) if a==b)


if __name__=='__main__':
    import sys
    problem_input = sys.stdin.readline().strip()
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
