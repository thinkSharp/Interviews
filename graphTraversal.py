import collections


class graph:
    def __init__(self, dict=None):
        if dict is None:
            dict = {}
        self.gdict = dict


def breadth_first_search(g, start, end):
    result = []
    queue = collections.deque()
    visited = set()

    queue.append(start)

    while queue:
        item = queue.popleft()
        if item not in visited:
            visited.add(item)
            result.append(item)
            if end in visited:
                return result

            if item in g.gdict:
                edges = g.gdict[item]
                for edge in edges:
                    if edge not in visited:
                        queue.append(edge)
    return []


def test_BFS():
    gdict = {'a': set(['b','c']), 'b': set(['a', 'd']), 'c' :set(['a','d']), 'd': set(['e']),'e': set(['f'])}
    g = graph(gdict)
    result = breadth_first_search(g, 'a', 'd')
    print(result)

    gdict = {'a': set(['b', 'c']), 'b': set(['a', 'd']), 'c': set(['a', 'g']), 'd': set(['e']), 'e': set(['h'])}
    g = graph(gdict)
    result = breadth_first_search(g, 'a', 'h')
    print(result)

test_BFS()

#==============================================================================================================

def depth_first_search(g, start, end):
    visited = set()
    result = []
    queue = collections.deque()

    queue.appendleft(start)
    while queue:
        item = queue.popleft()
        visited.add(item)
        result.append(item)
        if end in result:
            return result

        if item in g.gdict:
            edges = g.gdict[item]
            for edge in edges - visited:
                queue.appendleft(edge)
    return []

def test_DFS():
    gdict = {'a': set(['b','c']), 'b': set(['a', 'd']), 'c' :set(['a','d']), 'd': set(['e']),'e': set(['f'])}
    g = graph(gdict)
    result = depth_first_search(g, 'a', 'f')
    print(result)

    gdict = {'a': set(['b', 'c']), 'b': set(['a', 'd']), 'c': set(['a', 'g']), 'd': set(['e']), 'e': set(['h'])}
    g = graph(gdict)
    result = depth_first_search(g, 'a', 'h')
    print(result)

    gdict = {'a': set(['b', 'c']), 'b': set(['a', 'd']), 'c': set(['a', 'g']), 'd': set(['e']), 'e': set(['h'])}
    g = graph(gdict)
    result = depth_first_search(g, 'a', 'i')
    print(result)

#test_DFS()


def build_projects_order(projects, dependencies):
    if len(projects) == 0:
        return []

    order = []
    done = set()
    stack = collections.deque()

    i = 0
    for p in projects:
        stack.appendleft(p)
    while stack:
        item = stack.popleft()

        if item in done:
            continue

        if item in dependencies:
            stack.appendleft(item)
            for dependent in dependencies[item] - done:
                stack.appendleft(dependent)
            del dependencies[item]
        else:
            done.add(item)
            order.append(item)
    return order


def test_project_order():
    projects = ['g','b','c','d','a','f','e']
    dependencies = {'a': set(['f']), 'b': set(['f']), 'c': set(['d']), 'd': set(['a', 'b']), 'f': set(['e']),
                    'g': set(['c'])}
    result = build_projects_order(projects, dependencies)
    print(result)


test_project_order()






