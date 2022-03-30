import collections


def phrase_is_valid1(phrase):
    words = phrase.split(' ')
    counts = collections.Counter(words)
    return all(c<2 for c in counts.values())


def star1(phrases):
    count = 0
    for phrase in phrases:
        if phrase_is_valid1(phrase):
            count += 1
    return count


def phrase_is_valid2(phrase):
    words = [''.join(sorted(w)) for w in phrase.split(' ')]
    counts = collections.Counter(words)
    return all(c<2 for c in counts.values())


def star2(phrases):
    count = 0
    for phrase in phrases:
        if phrase_is_valid2(phrase):
            count += 1
    return count


if __name__=='__main__':
    import sys
    problem_input = [l.strip() for l in sys.stdin.readlines()]
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
