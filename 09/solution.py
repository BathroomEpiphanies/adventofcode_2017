import re
import json


def star1(stream):
    stream = re.sub(r'!.', r'', stream)
    stream = re.sub(r'<.*?>', r'', stream)
    stream = re.sub(r'[^{,}]', r'', stream)
    while True:
        stream,subs1 = re.subn(r'([^}]),', r'\1', stream)
        stream,subs2 = re.subn(r',([^{])', r'\1', stream)
        if not (subs1+subs2):
            break
    groups = json.loads(stream.translate(str.maketrans('{}','[]')))
    def score(groups, n):
        return n+sum((score(group, n+1) for group in groups))
    return score(groups, 1)


def star2(stream):
    stream = re.sub(r'!.', r'', stream)
    tmp = re.sub(r'<.*?>', r'<>', stream)
    return len(stream)-len(tmp)


if __name__=='__main__':
    import sys
    stream = sys.stdin.readline().strip()
    print(f'*1: {star1(stream)}')
    print(f'*2: {star2(stream)}')
