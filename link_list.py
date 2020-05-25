class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    total, power = 0, 0
    ptr1, ptr2 = l1, l2
    while ptr1 != None and ptr2 != None:
        total += (ptr1.val + ptr2.val) * pow(10, power)
        power += 1
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    if ptr1 != None:
        total += (ptr1.val) * pow(10, power)
        ptr1 = ptr1.next
    elif ptr2 != None:
        total += (ptr2.val) * pow(10, power)
        ptr2 = ptr2.next

    result, ptr = None, None
    while total > 0:
        val = total // 10
        total = total % 10
        node = ListNode(val)
        if result is None:
            result = node
        else:
            ptr.next = node
        ptr = node
    return result

a = -10
b = -a
print(pow(-2, -3))