def optimum_time_slot(slots):
    len_slots = len(slots)
    best_one_way = 0
    best_two_ways = 0
    for i in range(len_slots-1, -1, -1):
        current = slots[i] + best_two_ways
        current = max(current, best_one_way)
        best_two_ways = best_one_way
        best_one_way = current
    return best_one_way


def optimum_time_slots_recursive(slots):
    def get_best_slots(memo, slot):
        if slot >= len(slots):
            return 0
        if memo[slot] > 0:
            return memo[slot]
        with_current = slots[slot] + get_best_slots(memo, slot+2)
        without = get_best_slots(memo, slot+1)
        memo[slot] = max(with_current, without)
        return memo[slot]

    m = [0] * len(slots)
    return get_best_slots(m,0)


def test_best_slots():
    slots = [30,15,60,75,45,15,15,45]
    result = optimum_time_slot(slots)
    print(result)
    result2 = optimum_time_slots_recursive(slots)
    print(result2)
    assert(result == result2)


test_best_slots()