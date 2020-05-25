import collections


class Solution:
    def heapfy_max(self, a):
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

    def heap_pop(self, a):
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

    def heap_push(self, a, item):
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

    def leastInterval(self, tasks, n):

        counters = collections.Counter(tasks)
        total = len(tasks)
        h = [(-v, k) for k, v in counters.items()]
        h = self.heapfy_max(h)
        cooling = collections.deque()
        intervals = 0

        while total > 0:
            if len(cooling) > n:
                cool_task = cooling.popleft()
                if cool_task != 'idel' and counters[cool_task] > 0:
                    self.heap_push(h, (-counters[cool_task], cool_task))
            if len(h) > 0:
                task, h = self.heap_pop(h)
                counters[task[1]] -= 1
                cooling.append(task[1])
                total -= 1
            else:
                cooling.append('idel')
            intervals += 1
        return intervals


def test_intervals():
    sl = Solution()
    number = sl.leastInterval(['c', 'a', 'a', 'b', 'b', 'b'], 2)
    print(number)


#test_intervals()


def insert_interval3(intervals, newInterval):
    if len(intervals) == 0:
        return [newInterval]

    print(intervals)
    print(newInterval)
    result = []
    if len(intervals) == 1:
        current = intervals[0]
        if newInterval[0] <= current[1]:
            if newInterval[1] < current[1] and newInterval[0] < current[0] and newInterval[1] < current[0]:
                return [newInterval] + [current]
            elif current[1] > newInterval[1] > current[0] and newInterval[0] > current[0]:
                return [current]
            else:
                first = newInterval[0] if newInterval[0] < current[0] else current[0]
                last = newInterval[1] if newInterval[1] > current[1] else current[1]
                return [[first, last]]
        else:
            return [current] + [newInterval]

    new_interval_added = False
    for i in range(0, len(intervals)):
        previous = intervals[i]
        if not new_interval_added:
            if newInterval[0] <= previous[1]:
                if newInterval[1] < previous[1] and newInterval[0] < previous[0] and newInterval[1] < previous[0]:
                    result.append(newInterval)
                    result.append(previous)
                elif previous[1] > newInterval[1] > previous[0] and newInterval[0] > previous[0]:
                    result.append(previous)
                else:
                    first = newInterval[0] if newInterval[0] < previous[0] else previous[0]
                    last = newInterval[1] if newInterval[1] > previous[1] else previous[1]
                    result.append([first, last])

                new_interval_added = True
            else:
                result.append(intervals[i])
        else:
            previous = result[-1]
            current = intervals[i]
            if current[0] <= previous[1]:
                if newInterval[1] < current[1] and newInterval[0] < current[0] and newInterval[1] < current[0]:
                    result[-1] = [newInterval]
                    result.append(previous)
                elif current[1] > newInterval[1] > current[0] and newInterval[0] > current[0]:
                    continue
                else:
                    first = current[0] if current[0] < previous[0] else previous[0]
                    last = current[1] if current[1] > previous[1] else previous[1]
                    result[-1] = [first, last]
            else:
                result.append(current)

        if not new_interval_added:
            result.append(newInterval)
    return result


def insert_interval2(intervals, newInterval):
    if len(intervals) == 0:
        return [newInterval]
    if len(intervals) == 1:
        current = intervals[0]
        if newInterval[0] <= current[1]:
            if newInterval[1] < current[1] and newInterval[0] < current[0] and newInterval[1] < current[0]:
                return [newInterval] + [current]
            elif current[1] > newInterval[1] > current[0] and newInterval[0] > current[0]:
                return [current]
            else:
                first = newInterval[0] if newInterval[0] < current[0] else current[0]
                last = newInterval[1] if newInterval[1] > current[1] else current[1]
                return [[first, last]]
        else:
            return [current] + [newInterval]


def insert_interval(intervals, newInterval):
    def arrange_intervals(inters):
        result = []
        for i in range(0, len(inters)):
            if not result:
                result.append(inters[i])
            elif inters[i][0] <= result[-1][0]:
                result[-1][1] = max(result[-1][1], inters[1][1])
            else:
                result.append(inters[1])
        return result

    if len(intervals) == 0:
        return newInterval
    for i in range(len(intervals)):
        if intervals[i][0] > newInterval[0]:
            intervals.insert(i, newInterval)
            break
    intervals.append(newInterval)
    return arrange_intervals(intervals)

def test_insert_intervals():
    result = insert_interval([[2,5],[6,7],[8,9]], [0,1])
    print(result)
    result = insert_interval([[1,3],[6,9]], [2,5])
    print(result)
    result = insert_interval([[1,2],[3,5],[6,7],[8,10], [12,16]], [4,8])
    print(result)
    result = insert_interval([[1,5]], [0,3])
    print(result)
    result = insert_interval([[1,5]], [0,1])
    print(result)
    result = insert_interval([[1,5]], [0,0])
    print(result)
    result = insert_interval([[1,5]], [2,3])
    print(result)

test_insert_intervals()