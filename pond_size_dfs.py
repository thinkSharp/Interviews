import collections


def pond_size(m):
    row_len = len(m)
    if row_len == 0:
        return 0
    col_len = len(m[0])
    stack = collections.deque()
    visited = set()
    pond_sizes = {}

    for i in range(0, row_len):
        for j in range(0, col_len):
            stack.append((i, j, (i, j)))

    while stack:
        item = stack.popleft()
        i, j, ps = item
        visited.add((i, j))

        if m[i][j] != 0:
            continue

        if ps in pond_sizes:
            pond_sizes[ps] += 1
            # print("visited: {0}".format(visited))
            # print("item: {0}={1} => {2},{3}".format(item[2], pond_sizes[ps], i, j))
        else:
            pond_sizes[ps] = 1

        next_blocks = set(
            [(i, j + 1), (i, j - 1), (i + 1, j), (i - i, j), (i + 1, j + 1), (i - 1, j - 1), (i - 1, j + 1),
             (i + 1, j - 1)])
        for ni, nj in next_blocks - visited:
            if ni < 0 or ni >= row_len:
                continue
            if nj < 0 or nj >= col_len:
                continue
            if (ni, nj, ps) in stack:
                continue

            stack.appendleft((ni, nj, ps))
    size = set()
    for k, v in pond_sizes.items():
        size.add(v)
    return size


def test_pond_sizes():
    result = pond_size([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]])
    print(result)
    # assert(result == set([1,2,4]))
    result = pond_size([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0], [0, 0, 0, 1]])
    print(result)


test_pond_sizes()
