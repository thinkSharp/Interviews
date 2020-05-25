import collections
import time


class Disk:
    def __init__(self, size, pole, previous):
        self.size = size
        self.pole = pole
        self.previous = previous

    def __str__(self):
        return "size: " + str(self.size) + ",pole: " + str(self.pole) + ",previous: " + str(self.previous) + ";"

    def __repr__(self):
        return "size: " + str(self.size) + ",pole: " + str(self.pole) + ",previous: " + str(self.previous) + ";"


def moveTheTower():
    def checkPoleAndAdd(disk, n_pole, s):
        d = Disk(disk.size, n_pole, disk.pole)
        if not s:
            path.append(d)
            s.appendleft(d)
            return True
        elif disk.size < s[0].size:
            path.append(d)
            s.appendleft(d)
            return True
        return False

    s1 = collections.deque()
    s1.appendleft(Disk(5,1,0))
    s1.appendleft(Disk(4,1,0))
    s1.appendleft(Disk(3,1,0))
    s1.appendleft(Disk(2,1,0))
    s1.appendleft(Disk(1,1,0))

    s2 = collections.deque()
    s3 = collections.deque()
    current = s1
    previous_no = 0
    path = []
    visited = []
    while True:
        move_disk = False
        if len(current) == 0:
            break

        disk = current.popleft()
        if disk.pole == 1:
            if disk.previous == 2:
                move_disk = checkPoleAndAdd(disk, 3, s3)
            elif disk.previous == 3:
                move_disk = checkPoleAndAdd(disk, 2, s2)
            else:
                move_disk = checkPoleAndAdd(disk, 2, s2)
                if not move_disk:
                    move_disk = checkPoleAndAdd(disk, 3, s3)
        elif disk.pole == 2:
            if disk.previous == 1:
                move_disk = checkPoleAndAdd(disk, 3, s3)
            else:
                move_disk = checkPoleAndAdd(disk, 1, s1)
        else:
            if disk.previous == 2:
                move_disk = checkPoleAndAdd(disk, 1, s1)
            else:
                move_disk = checkPoleAndAdd(disk, 2, s2)

        if len(s3) == 5:
            return path

        if not move_disk:
            current.appendleft(disk)

        print(s1)
        print(s2)
        print(s3)
        time.sleep(1)
        print('---------')

        if not move_disk or len(current) == 0:
            if current == s1 and len(s2) != 0 and previous_no != 2:
                current = s2
                previous_no = 1
            elif current == s1 and len(s3) != 0 and previous_no != 3:
                current = s3
                previous_no = 1
            elif current == s2 and len(s1) != 0 and previous_no != 1:
                current = s1
                previous_no = 2
            elif current == s2 and len(s3) != 0 and previous_no != 3:
                current = s3
                previous_no = 2
            elif current == s3 and len(s1) != 0 and previous_no != 1:
                current = s1
                previous_no = 3
            elif current == s3 and len(s2) != 0 and previous_no != 2:
                current = s2
                previous_no = 3
    return []

class Tower:
    def __init__(self, i):
        self.stack = collections.deque()
        self.i = i

    def add(self, d):
        if len(self.stack) != 0 and self.stack[0] <= d:
            print("Invalid disk %d on tower %d", d, self.i)
        else:
            self.stack.appendleft(d)

    def moveTopTo(self, t):
        if len(self.stack) > 0:
            top = self.stack.popleft()
            t.add(top)

    def moveDisks(self, n, destination, buffer):
        if n > 0:
            self.moveDisks(n-1, buffer, destination)
            self.moveTopTo(destination)
            print("Moving n %d from self.index %d to destination.index %d", n, self.i, destination.i)
            self.moveDisks(n-1, destination, self)

    def print(self):
        for i in range(0, len(self.stack)):
            print(self.stack[i], end=',')
        print('')

def hanoi2(n,src,dst,tmp, loc):
    print("incoming: =>{0}, src {1}, dst {2}, tmp {3}, loc {4}".format(n, src,dst, tmp, loc) )
    if n <= 0:
        pass
    else:
        for h in hanoi2(n-1, src, tmp, dst, 1):
            yield  h
        yield(n, src, dst, loc)
        for h in hanoi2(n-1, tmp, dst, src, 2):
            yield  h

#result = [h for h in hanoi2(3,1,3,2,0)]
#print(result)

def hanoi(n, src, dst, tmp, loc):
    print("incoming: =>{0}, src {1}, dst {2}, tmp {3}, loc {4}".format(n, src,dst, tmp, loc) )
    if n <= 0:
        print("leaving {0},{1}".format(n,loc))
        return
    hanoi(n-1, src, tmp, dst, 1)
    print(n, src, dst, tmp, loc)
    hanoi(n-1, tmp, dst, src, 2)

hanoi(3, 1, 3, 2, 0)

def test_towerOfHanoi():
    towers = [Tower(1), Tower(2), Tower(3)]
    for i in range(1, 6):
        towers[0].add(i)

    towers[0].moveDisks(5, towers[2], towers[1])

    print(towers[2].print())

#test_towerOfHanoi()