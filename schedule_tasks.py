import collections
import queue
class Task_Scheduler(object):
    def __init__(self, tasks, idel):
        self.counter = collections.Counter(tasks)
        self.heap = queue.PriorityQueue(len(self.counter))
        self.cooling = collections.deque()
        self.idel = idel
        self.result = []
        self.total = len(tasks)
        self.interval = 0
        print(self.counter)
        for k,v in self.counter.items():
            self.heap.put((-v, k))

    def leastIntervals(self):

        while self.total > 0:
            if len(self.cooling) > self.idel:
                cool_item = self.cooling.popleft()
                if cool_item != 'idel' and self.counter[cool_item] > 0:
                    self.heap.put((-self.counter[cool_item], cool_item))

            if not self.heap.empty():
                v, item = self.heap.get()
                self.counter[item] -= 1
                self.result.append(item)
                self.cooling.append(item)
                self.total -= 1
            else:
                self.result.append('idel')
                self.cooling.append('idel')


        return self.result


def test_task_scheduler():
    t = Task_Scheduler(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)
    intervals = t.leastIntervals()
    print(intervals)

#test_task_scheduler()

def exclusiveTime(n, logs):
    """
    :type n: int
    :type logs: List[str]
    :rtype: List[int]
    goal: return the exclusive time of each functions
    steps:
        loop through the log entries
            if task_id == stack.peek[0])
                pop that task and calculate the total time
                add this task into result array
            else:
                push that task in the stack

    """
    ln = len(logs)
    if n == 0 or ln == 0:
        return []
    result = [0] * n
    stack = collections.deque()
    st = logs[0].split(':')
    stack.append(int(st[0]))
    prev = int(st[2])
    for i in range(ln):
        item = logs[i].split(':')
        log_id, time = int(item[0]), int(item[2])
        if item[1] == 'start':
            if len(stack) != 0:
                result[stack[-1]] += time - prev

            stack.append(log_id)
            prev = time
        else:
            result[stack[-1]] += time - prev + 1
            stack.pop()
            prev = time + 1
    return result



def test_execlusiveTime():
    task = exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])
    print(task)
    task = exclusiveTime(4, ["0:start:0","2:start:2","2:end:5","1:start:6","3:start:7","3:end:7","1:end:8","0:end:9"])
    print(task)
    task = exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"])
    print(task)


#test_execlusiveTime()

def maximumSwap(num):
    if num == 0:
        return
    lst = list(map(int, str(num)))
    last = collections.defaultdict(int, {x: i for i, x in enumerate(lst)})
    for i, x in enumerate(lst):
        for d in range(9, x, -1):
            if last[d] > i:
                lst[i], lst[last[d]] = lst[last[d]], lst[i]
                return int(''.join(map(str, lst)))
    return num

def test_max_swap():
    result = maximumSwap(1235)
    print(result)
    result = maximumSwap(9937)
    print(result)
    result = maximumSwap(987612345)
    print(result)

#test_max_swap()


class DSU:
    def __init__(self):
        self.par = range(1001)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

a = DSU()


print(a.par)
print(a.par[2])