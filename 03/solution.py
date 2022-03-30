def next_state(position, heading):
    position += heading
    if heading==+0+1j:
        return (position,heading) if position.imag<  position.real else (position,heading*1j)
    if heading==-1+0j:
        return (position,heading) if position.real> -position.imag else (position,heading*1j)
    if heading==+0-1j:
        return (position,heading) if position.imag>  position.real else (position,heading*1j)
    if heading==+1+0j:
        return (position,heading) if position.real<=-position.imag else (position,heading*1j)
    raise Exception('Invalid heading')


def star1(number):
    position,heading = +0+0j,+1+0j
    for _ in range(1,number):
        position,heading = next_state(position, heading)
    return round(abs(position.real)+abs(position.imag))


def star2(number):
    if number==0: return 1
    dirs = [+1+0j,+1+1j,+0+1j,-1+1j,-1+0j,-1-1j,+0-1j,+1-1j]
    position,heading = +0+0j,+1+0j
    memory = {position: 1}
    while True:
        position,heading = next_state(position, heading)
        memory[position] = sum(memory.get(position+d,0) for d in dirs)
        if memory[position]>number:
            return memory[position]
    raise Exception('You should not be here')


if __name__=='__main__':
    import sys
    problem_input = int(sys.stdin.readline())
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
