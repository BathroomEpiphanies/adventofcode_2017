import pprint
import re


def parse(lines):
    graph = {}
    for line in lines:
        tokens = line.split(' -> ')
        graph[tokens[0].split(' ')[0]] = {
            'weight':   int(tokens[0].split(' ')[1][1:-1]),
            'children': tokens[1].split(', ') if len(tokens)>1 else [],
        }
    #pprint.pprint(graph, indent=4)
    return graph


def star1(graph):
    nodes = graph.keys()
    for node,data in graph.items():
        nodes -= set(data['children'])
    #pprint.pprint(nodes, indent=4)
    if len(nodes)>1:
        raise Exception('More than one root node')
    return list(nodes)[0]


def star2(graph):
    pprint.pprint(graph, indent=4)
    def recurse(node):
        if not graph[node]['children']:
            graph[node]['branch'] = graph[node]['weight']
        else:
            graph[node]['branch'] = graph[node]['weight'] + sum(recurse(n) for n in graph[node]['children'])
        if len(set([graph[n]['branch'] for n in graph[node]['children']]))>1:
            print([(graph[n]['branch'],graph[n]['weight']) for n in graph[node]['children']])
            return
        return graph[node]['branch']
        
    root = star1(graph)
    return recurse(root)
    #print('hopp')
    #pprint.pprint(graph, indent=4)
    #return recurse(root)



if __name__=='__main__':
    import sys
    graph = parse([l.strip() for l in sys.stdin.readlines()])
    print(f'*1: {star1(graph)}')
    print(f'*2: {star2(graph)}')
