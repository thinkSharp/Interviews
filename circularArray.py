class CircularArray:
    def __init__(self, size):
        self.size = size
        self.index = -1
        self.lst = [0] * size

    def __iter__(self):
        self.iter_index = -1
        return self

    def __next__(self):
        if self.iter_index + 1 < self.size:
            self.iter_index += 1
            return self.lst[self.iter_index]

        else:
            self.iter_index = 0
            return self.lst[self.iter_index]
    def add(self, data):
        if self.index + 1 < self.size:
            self.index += 1
            self.lst[self.index] = data
        else:
            self.index = 0
            self.lst[self.index] = data

def test_circularArray():
    c_array = CircularArray(10)
    for i in range(0, 10):
        c_array.add(i)

    for i in c_array:
        print(i)

#test_circularArray()

import random
print(random.sample(range(0,100), 10))