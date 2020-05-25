class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp

    def addNode(self, node):
        if not isinstance(node, Node):
            print("Invalid node Instance")
            return

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def add(self, data):

        node = Node(data)
        self.addNode(node)

    def add_unique(self, data):
        if self.head is None:
            self.add(data)
            return True

        ptr = self.head

        while ptr is not None:
            if ptr.data == data:
                return False
            else:
                ptr = ptr.next
        self.add(data)
        return True

    def print_list(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='')
            print(",", end=' ')
            ptr = ptr.next
        print("")

    def node_count(self):
        count = 0
        ptr = self.head
        while ptr is not None:
            count += 1
            ptr = ptr.next

        return count

    def print_kth_item(self, k):
        counter = 0
        ptr = self.head
        while ptr is not None:
            counter += 1
            ptr = ptr.next
        if 0 <= k > counter:
            print("Invalid kth")
            return

        skip = counter - k
        counter = 0
        ptr = self.head
        while ptr is not None:
            counter += 1

            if counter > skip:
                print("kth " + str(k) + " data is:" + str(ptr.data))
                return
            ptr = ptr.next

    def delete_one_of_middle(self):
        ptr = self.head
        if self.head == self.tail:
            return
        ptr = ptr.next
        self.head.next = ptr.next

    def partition_linked_list(self, point):
        ptr = self.head
        left_ptr = None
        left_ptr_tail = None
        right_ptr = None
        right_ptr_tail = None

        while ptr is not None:
            node = Node(ptr.data)
            if node.data < point:
                if left_ptr is None:
                    left_ptr = node
                else:
                    left_ptr_tail.next = node
                left_ptr_tail = node

            elif node.data == point:
                if right_ptr is None:
                    right_ptr = node
                    right_ptr_tail = node
                else:
                    temp = right_ptr
                    right_ptr = node
                    right_ptr.next = temp
            else:
                if right_ptr is None:
                    right_ptr = node
                else:
                    right_ptr_tail.next = node
                right_ptr_tail = node

            ptr = ptr.next
        left_ptr_tail.next = right_ptr
        self.head = left_ptr


def reverseLinkedList(linked_list):
    if not isinstance(linked_list, SingleLinkedList):
        print("Invalid linked list")
        return

    reserve_linked_list = SingleLinkedList()
    ptr = linked_list.head
    while ptr is not None:
        reserve_linked_list.add_front(ptr.data)
        ptr = ptr.next

    return reserve_linked_list


def reverseAddTwoNumbers(linked_list1, linked_list2):
    l1 = reverseLinkedList(linked_list1)
    l1.print_list()
    l2 = reverseLinkedList(linked_list2)
    l2.print_list()
    result = addTwoNumbers(l1, l2)
    return result


def addTwoNumbers(linked_list1, linked_list2):
    if not isinstance(linked_list1, SingleLinkedList):
        print("Invalid linked list")
        return

    if not isinstance(linked_list2, SingleLinkedList):
        print("Invalid linked list")
        return

    power = 0
    left_sum = 0
    right_sum = 0
    ptr_left = linked_list1.head
    ptr_right = linked_list2.head
    added = False
    while True:
        if ptr_left is not None:
            left_sum += ptr_left.data * pow(10, power)
            ptr_left = ptr_left.next
            added = True
        if ptr_right is not None:
            right_sum += ptr_right.data * pow(10, power)
            ptr_right = ptr_right.next
            added = True
        if added:
            power += 1
            added = False
        else:
            break
    total = left_sum + right_sum
    new_list = SingleLinkedList()
    power -=1
    while total > 0:
        divisor = pow(10, power)
        if divisor == 0:
            value = total
            total = 0
        else:
            value = total // divisor
            total = total % divisor
        power -= 1
        new_list.add(value)
    return new_list


def isPalindrome(linked_list):
    if not isinstance(linked_list, SingleLinkedList):
        print("Invalid linked list")
        return False

    fast = linked_list.head
    slow = linked_list.head
    middle = 1
    odd_link = False
    while True:
        if fast.next is not None:
            fast = fast.next
        else:
            odd_link = True
            break

        if fast.next is not None:
            fast = fast.next
        else:
            break
        slow = slow.next
        middle += 1

    if odd_link:
        middle -= 1

    lst = [] * middle
    ptr = linked_list.head
    for i in range(0, middle):
        if ptr is None:
            break
        lst.insert(0, ptr.data)
        ptr = ptr.next
    i = 0
    slow = slow.next
    while slow is not None:
        if i >= middle:
            return False

        if slow.data == lst[i]:
            slow = slow.next
            i += 1
        else:
            return False
    return True


def removeDuplicate(linked_list):
    if not isinstance(linked_list, SingleLinkedList):
        print("Invalid linked list")
        return linked_list
    clean_linked_list = SingleLinkedList()
    ptr = linked_list.head
    while ptr is not None:
        clean_linked_list.add_unique(ptr.data)
        ptr = ptr.next

    return clean_linked_list


def detectIntersectNode(linked_list1, linked_list2):
    if not isinstance(linked_list1, SingleLinkedList):
        print("Invalid linked list 1")
        return None
    if not isinstance(linked_list2, SingleLinkedList):
        print("Invalid linked list 2")
        return None

    len_1 = linked_list1.node_count()
    len_2 = linked_list2.node_count()

    ptr_1 = linked_list1.head
    ptr_2 = linked_list2.head
    if len_1 > len_2:
        for i in range(0, len_1 - len_2):
            ptr_1 = ptr_1.next
    elif len_2 > len_1:
        for i in range(0, len_2 - len_1):
            ptr_2 = ptr_2.next

    while True:
        if ptr_1 is None and ptr_2 is None:
            return None
        elif ptr_1 is None:
            print("Invalid scenario ptr_1 is None first")
            return None
        elif ptr_2 is None:
            print("Invalid scenario ptr_2 is None first")
            return None

        if ptr_1 == ptr_2:
            return ptr_1.data
        else:
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next


def detect_circular(linked_list):
    if not isinstance(linked_list, SingleLinkedList):
        print("Invalid linked list")
        return None
    fast = linked_list.head
    slow = linked_list.head
    while True:
        if fast.next is None:
            return None
        if fast.next == slow:
            return fast.next.data
        fast = fast.next
        if fast.next == slow:
            return fast.next.data

        print("Fast: " + str(fast.data) + ", slow: " + str(slow.data))
        fast = fast.next
        slow = slow.next


def test_circular_link_list():
    node = Node('C')
    link_list2 = SingleLinkedList()
    link_list2.add('A')
    link_list2.add('B')
    link_list2.add('D')
    link_list2.add('EE')
    link_list2.add('AA')
    link_list2.add('BC')
    link_list2.add('AD')
    link_list2.add('BJ')
    link_list2.addNode(node)
    link_list2.add('D')
    link_list2.add('F')
    link_list2.addNode(node)

    print(detect_circular(link_list2))


#test_circular_link_list()


def test_intersection_point():
    node = Node(31)
    link_list2 = SingleLinkedList()
    link_list2.add(2)
    link_list2.add(1)
    link_list2.addNode(node)

    link_list = SingleLinkedList()
    link_list.add(7)
    link_list.add(1)
    link_list.add(6)
    link_list.add(6)
    link_list.addNode(node)
    link_list.add(1)
    link_list.add(7)
    link_list.print_list()
    print(detectIntersectNode(link_list, link_list2))

    link_list3 = SingleLinkedList()
    link_list3.add(7)
    link_list3.add(1)

    print(isPalindrome(link_list3))

    link_list4 = SingleLinkedList()
    link_list4.add(7)
    link_list4.add(7)

    print(detectIntersectNode(link_list3, link_list4))


#test_intersection_point()


def test_is_palindrome():
    link_list = SingleLinkedList()
    link_list.add(7)
    link_list.add(1)
    link_list.add(6)
    link_list.add(6)
    link_list.add(1)
    link_list.add(7)

    print(isPalindrome(link_list))

    link_list2 = SingleLinkedList()
    link_list2.add(7)
    link_list2.add(1)
    link_list2.add(6)
    link_list2.add(4)
    link_list2.add(6)
    link_list2.add(1)
    link_list2.add(7)

    print(isPalindrome(link_list2))

    link_list3 = SingleLinkedList()
    link_list3.add(7)
    link_list3.add(1)

    print(isPalindrome(link_list3))


    link_list3 = SingleLinkedList()
    link_list3.add(7)
    link_list3.add(7)

    print(isPalindrome(link_list3))

#test_is_palindrome()

def test_add_two_linked_list():
    link_list = SingleLinkedList()
    link_list.add(7)
    link_list.add(1)
    link_list.add(6)

    link_list2 = SingleLinkedList()
    link_list2.add(5)
    link_list2.add(9)
    link_list2.add(2)

    lst = addTwoNumbers(link_list, link_list2)
    lst.print_list()

    link_list = SingleLinkedList()
    link_list.add(7)
    link_list.add(1)
    link_list.add(6)

    link_list2 = SingleLinkedList()
    link_list2.add(0)
    link_list2.add(5)
    link_list2.add(9)
    link_list2.add(2)

    lst = addTwoNumbers(link_list, link_list2)
    lst.print_list()

    link_list = SingleLinkedList()
    link_list.add(6)
    link_list.add(1)
    link_list.add(7)

    link_list2 = SingleLinkedList()
    link_list2.add(2)
    link_list2.add(9)
    link_list2.add(5)
    lst = reverseAddTwoNumbers(link_list, link_list2)
    lst.print_list()

#test_add_two_linked_list()

def test():
    link_list = SingleLinkedList()
    link_list.add(5)
    link_list.add(10)
    link_list.add(20)
    link_list.add(7)
    link_list.add(15)
    link_list.add(20)
    link_list.add(3)
    link_list.add(10)

    link_list.print_list()
    link_list.partition_linked_list(10)
    link_list.print_list()

    new_list = removeDuplicate(link_list)

    new_list.print_list()

    link_list.print_kth_item(3)
    link_list.print_kth_item(7)
    link_list.print_kth_item(20)
    link_list.print_kth_item(1)

    link_list.delete_one_of_middle()
    link_list.print_list()


#test()
