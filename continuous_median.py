import math


class Heap:
    def __init__(self, is_min_heap, size):
        self.data_list = [0] * size
        self.is_min_heap = is_min_heap
        self.current_pos = 0

    def print(self):
        print(self.data_list)

    def length(self):
        return self.current_pos

    def peek(self):
        if self.current_pos == 0:
            return None

        return self.data_list[0]

    def pop(self):
        if self.current_pos == 0:
            return None

        val = self.data_list[0]
        self.data_list[0] = self.data_list[self.current_pos - 1]
        self.data_list[self.current_pos - 1] = 0
        print("Popping: {0}:{1},{2}".format(val, self.data_list[0], self.data_list[self.current_pos-1]))
        self.current_pos -= 1
        self.__adjust_children__()
        print("After adjusting children: {0}".format(self.data_list[0]))
        return val

    def __adjust_children__(self):
        def swap(i, j):
            self.data_list[i], self.data_list[j] = self.data_list[j], self.data_list[i]

        def adjust_children(parent_index):
            child_1 = parent_index * 2 + 1
            child_2 = child_1 + 1

            if child_1 >= self.current_pos:
                return
            if child_2 >= self.current_pos:
                selected_child = child_1
            else:
                if self.is_min_heap:
                    selected_child = child_1 \
                        if self.data_list[child_1] < self.data_list[child_2] \
                        else child_2
                else:
                    selected_child = child_1 \
                        if self.data_list[child_1] > self.data_list[child_2] \
                        else child_2
            #print("Before Values: {0},{1},{2},{3}".format(self.data_list[parent_index], self.data_list[selected_child], parent_index, selected_child))
            if self.is_min_heap:
                if self.data_list[parent_index] > self.data_list[selected_child]:
                    swap(parent_index, selected_child)
                    adjust_children(selected_child)
            else:
                if self.data_list[parent_index] < self.data_list[selected_child]:
                    swap(parent_index, selected_child)
                    adjust_children(selected_child)
            #print("Min_heap:{0}, child1: {1}, child2:{2}, pos:{3}, selected:{4}, parent:{5}".format(self.is_min_heap, child_1, child_2, self.current_pos, selected_child, parent_index))
            #print("After Values: {0},{1}".format(self.data_list[parent_index], self.data_list[selected_child]))
        adjust_children(0)

    def insert(self, data):
        if self.current_pos >= len(self.data_list):
            self.data_list.append(data)
        else:
            self.data_list[self.current_pos] = data
        self.__adjust_parent(self.current_pos)
        self.current_pos += 1

    def __adjust_parent(self, child_index):
        def swap(i, j):
            self.data_list[i], self.data_list[j] = self.data_list[j], self.data_list[i]

        def adjust_parent(index):
            if index == 0:
                return
            parent_index = math.floor(index / 2)

            if self.is_min_heap:
                if self.data_list[parent_index] > self.data_list[index]:
                    swap(parent_index, index)
                    adjust_parent(parent_index)
            else:
                if self.data_list[parent_index] < self.data_list[index]:
                    swap(parent_index, index)
                    adjust_parent(parent_index)

            print("min_heap:{0},index:{1}, parent:{2}, {3} and {4}".format(self.is_min_heap, index, parent_index,
                                                                       self.data_list[index],
                                                                       self.data_list[parent_index]))
        adjust_parent(child_index)


def median_for_running_series(series):
    def get_median():
        if min_heap.length() == max_heap.length() == 0:
            return 0
        elif min_heap.length() == max_heap.length():
            return (min_heap.peek() + max_heap.peek()) / 2
        elif max_heap.length() > min_heap.length():
            return max_heap.peek()
        else:
            min_heap.peek()

    def insert(data):
        if min_heap.length() == max_heap.length():
            if min_heap.peek() is not None and data > min_heap.peek():
                max_heap.insert(min_heap.pop())
                min_heap.insert(data)
            else:
                max_heap.insert(data)
        else:
            if data < max_heap.peek():
                min_heap.insert(max_heap.pop())
                max_heap.insert(data)
            else:
                min_heap.insert(data)

    min_heap = Heap(True, 10)
    max_heap = Heap(False, 10)
    for i in series:
        print("inserting {0}".format(i))
        insert(i)
        print("Starting - MinHeap")
        print(min_heap.print())
        print("Median")
        print(get_median())
        print("Ending - maxHeap")
        print(max_heap.print())



def test_continuous_median():
    series = [3,5,7,1,9,4,2,1]
    median_for_running_series(series)


test_continuous_median()


