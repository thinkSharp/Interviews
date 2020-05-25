import collections

'''
Depth first search approach was used
'''


def pathForRobot(block_grids, start, end):
    visited = set()
    path = []
    stack = collections.deque()
    stack.appendleft(start)
    ei, ej = end
    while stack:
        point = stack.popleft()
        visited.add(point)
        path.append(point)
        if point == end:
            return path
        i, j = point
        right_move = (i, j + 1)
        down_move = (i + 1, j)
        for move in (right_move, down_move):
            mi, mj = move
            if mi > ei or mj > ej:
                continue
            if move in block_grids:
                continue
            if move in visited:
                continue
            stack.appendleft(move)
    return []


def test_pathForRobot():
    block_grids = [(0,2),(1,1),(3,0),(2,2)]
    result = pathForRobot(block_grids, (0,0),(3,3))
    print(result)


test_pathForRobot()