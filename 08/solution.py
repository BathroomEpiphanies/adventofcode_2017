def star(lines):
    variables = {}
    max_variables = {}
    for line in lines:
        variable = line.split(' ')[0]
        variables[variable] = None
        max_variables[variable] = 0
        exec(f'{variable} = 0')
    for line in lines:
        variable = line.split(' ')[0]
        max_variables[variable] = max(max_variables[variable], eval(variable))
        exec(line.replace('inc', '+=').replace('dec', '-=')+' else 0')
    for variable in variables:
        variables[variable] = eval(variable)
    return max(variables.values()),max(max_variables.values())


def star1(program):
    return star(program)[0]


def star2(program):
    return star(program)[1]


if __name__=='__main__':
    import sys
    answers = star([l.strip() for l in sys.stdin.readlines()])
    print(f'*1: {answers[0]}')
    print(f'*2: {answers[1]}')
