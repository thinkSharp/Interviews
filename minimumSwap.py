def minimumSwaps(arr):
    def heapify_max(a):
        array_len = i = len(a) - 1

        def swap(parent, c1, c2):
            if a[parent] < a[c1] or a[parent] < a[c2]:
                if a[c1] > a[c2]:
                    a[parent], a[c1] = a[c1], a[parent]
                    check_children(c1)
                else:
                    a[parent], a[c2] = a[c2], a[parent]
                    check_children(c2)

        def check_children(item_index):
            child_1_index = item_index * 2 + 1
            child_2_index = child_1_index + 1
            if child_1_index <= array_len and child_2_index <= array_len:
                swap(item_index, child_1_index, child_2_index)
            elif child_1_index <= array_len:
                if a[item_index] < a[child_1_index]:
                    a[item_index], a[child_1_index] = a[child_1_index], a[item_index]
                    check_children(child_1_index)

        while i >= 0:
            check_children(i)
            i -= 1
        return a

    def heap_pop(a):
        array_len = len(a) - 1

        def swap(parent, c1, c2):
            if a[parent] < a[c1] or a[parent] < a[c2]:
                if a[c1] > a[c2]:
                    a[parent], a[c1] = a[c1], a[parent]
                    check_children(c1)
                else:
                    a[parent], a[c2] = a[c2], a[parent]
                    check_children(c2)

        def check_children(item_index):
            child_1_index = item_index * 2 + 1
            child_2_index = child_1_index + 1
            if child_1_index <= array_len and child_2_index <= array_len:
                swap(item_index, child_1_index, child_2_index)
            elif child_1_index <= array_len:
                if a[item_index] < a[child_1_index]:
                    a[item_index], a[child_1_index] = a[child_1_index], a[item_index]
                    check_children(child_1_index)

        if len(a) <= 0:
            return 0
        top = a[0]
        a[0] = a[array_len]
        check_children(0)
        a = a[:-1]
        return top, a

    def heap_push(a, item):
        a.append(item)
        array_len = len(a) - 1

        def check_parent(item_index):
            parent_index = (item_index // 2) - 1 if item_index % 2 == 0 else item_index // 2
            if item_index == 0 or parent_index == item_index:
                return

            if a[parent_index] < a[item_index]:
                a[parent_index], a[item_index] = a[item_index], a[parent_index]
                check_parent(parent_index)

        check_parent(array_len)
        return a

    def calculate_cost(item, index):
        c = item - 1 - index
        return c, index, item - 1

    arr_len = len(arr)
    cost = []
    swap_count = 0

    for i, item in enumerate(arr):
        c = calculate_cost(item, i)
        if c[0] > 0:
            cost = heap_push(cost, c)

    while True:
        print(str(cost))
        if len(cost) == 0:
            break
        top, cost = heap_pop(cost)
        m_cost, max_index, replace_index = top
        if m_cost == 0:
            continue
        if arr[max_index] -1 == max_index:
            continue
        if arr[replace_index] -1 == replace_index:
            continue

        swap_count += 1
        arr[max_index], arr[replace_index] = arr[replace_index], arr[max_index]
        c = calculate_cost(arr[max_index], max_index)
        if c[0] > 0:
            cost = heap_push(cost, c)
        c = calculate_cost(arr[replace_index], replace_index)
        if c[0] > 0:
            cost = heap_push(cost, c)

    return swap_count
def minimumSwaps1(arr):
    def calculate_cost(item, index):
        c = item - 1 - index
        return c
    arr_len = len(arr)
    cost = [0] * arr_len
    swap_count = 0
    max_index = 7
    replace_index = 0
    max_cost = len(arr) * -1
    for i, item in enumerate(arr):
        cost[i] = calculate_cost(item, i)
        if max_cost < cost[i] != 0:
            max_cost = cost[i]
            max_index = i
            replace_index = arr[i] -1
    while True:
        print(str(cost))
        if max_cost == len(arr) * -1:
            break
        swap_count += 1
        arr[max_index], arr[replace_index] = arr[replace_index], arr[max_index]
        cost[max_index] = calculate_cost(arr[max_index], max_index)
        cost[replace_index] = calculate_cost(arr[replace_index], replace_index)
        max_cost = len(arr) * -1
        for i in range(0, len(cost)):
            if max_cost < cost[i] != 0:
                max_cost = cost[i]
                max_index = i
                replace_index = arr[i] - 1


    return swap_count

result = minimumSwaps([1, 2, 3, 4, 5])
print(result)
assert(result == 0)
result = minimumSwaps([4, 3, 1, 2])
print(result)
assert(result == 3)
result = minimumSwaps([4, 3, 5, 1, 2])
print(result)
assert(result == 3)
result = minimumSwaps([1, 3, 5, 2, 4, 6, 7])
print(result)
assert(result == 3)
result = minimumSwaps([3, 7, 6, 9, 1, 8, 10, 4, 2, 5])
print(result)
assert(result == 9)
result = minimumSwaps([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(result)
assert(result == 10)
