def build_dive_board(planks, small, large):
    def build_board(remaining_planks, length, total):
        if remaining_planks == 0:
            total.add(length)
            return
        build_board(remaining_planks -1, length + small, total)
        build_board(remaining_planks-1, length + large, total)
    no_lengths = set()
    build_board(planks, 0, no_lengths)
    return no_lengths

def build_dive_board2(planks, small,large):
    def build_board(remaining_planks, length, total, cache):
        if remaining_planks == 0:
            total.add(length)
            return
        key = str(remaining_planks) + ' ' + str(length)
        if key in cache:
            return

        build_board(remaining_planks - 1, length + small, total, cache)
        build_board(remaining_planks - 1, length + large, total, cache)
        cache.add(key)

    no_lengths = set()
    build_board(planks, 0, no_lengths, set())
    return no_lengths


def build_dive_board3(planks, small, large):
    lengths = set()
    for s in range(0, planks+1):
        l = planks - s
        length = small * s + large * l
        lengths.add(length)
    return lengths


def build_dive_board4(planks, small,medium, large):
    def build_board(remaining_planks, length, total, cache):
        if remaining_planks == 0:
            total.add(length)
            return
        key = str(remaining_planks) + ' ' + str(length)
        if key in cache:
            return

        build_board(remaining_planks - 1, length + small, total, cache)
        build_board(remaining_planks - 1, length + medium, total, cache)
        build_board(remaining_planks - 1, length + large, total, cache)
        cache.add(key)

    no_lengths = set()
    build_board(planks, 0, no_lengths, set())
    return no_lengths


def build_dive_board5(planks, small, medium, large):
    lengths = set()
    for s in range(0, planks+1):
        s_planks = planks - s
        for m in range(0, planks+1):
            l = s_planks - m
            if l >= 0:
                length = small * s + medium * m + large * l
                lengths.add(length)
    return lengths

def test_build_dive_board():
    result = build_dive_board(15, 3, 5)
    print(result)

    result = build_dive_board2(15, 3, 5)
    print(result)

    result = build_dive_board3(15, 3, 5)
    print(result)

    result = build_dive_board4(15, 3, 4, 5)
    print(result)

    result = build_dive_board5(15, 3, 4, 5)
    print(result)

test_build_dive_board()