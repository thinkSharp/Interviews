import link_list_2_0


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node):
        self.root = node

    # left, current, right
    def print_in_order(self):
        def in_order(node):
            if node is None:
                return
            in_order(node.left)
            print(node.data, end=' ')
            in_order(node.right)

        if self.root is None:
            return
        print("In-Order: left, center, right")
        in_order(self.root)

    # current, left, right
    def print_pre_order(self):
        def pre_order(node):
            if node is None:
                return
            print(node.data, end=' ')
            pre_order(node.left)
            pre_order(node.right)

        if self.root is None:
            return
        print("Pre-Order: current, left, right")
        pre_order(self.root)

    # left, right, current
    def print_post_order(self):
        def post_order(node):
            if node is None:
                return
            post_order(node.left)
            post_order(node.right)
            print(node.data, end=' ')

        if self.root is None:
            return
        print("Post-Order: left, right, center")
        post_order(self.root)

    def create_linked_list_at_each_depth(self):

        def add_to_link_list(lst, node, depth):
            if node is None:
                return

            ll = lst[depth]
            ll.add(node.data)
            if depth + 1 >= len(lst):
                child_ll = link_list_2_0.SingleLinkedList()
                lst.append(child_ll)

            add_to_link_list(lst, node.left, depth + 1)
            add_to_link_list(lst, node.right, depth + 1)

        if self.root is None:
            return []

        root_ll = link_list_2_0.SingleLinkedList()
        result = [root_ll]
        add_to_link_list(result, self.root, 0)
        return result


def checkBalance(tree):
    def check_balance(node):
        if node is None:
            return 0
        left = right = 0
        if node.left is not None:
            left = check_balance(node.left) + 1
        if node.right is not None:
            right = check_balance(node.right) + 1
        return left if left > right else right

    if tree.root is None:
        return True
    root_l = root_r = 0
    if tree.root.left is not None:
        root_l = check_balance(tree.root.left) + 1
    if tree.root.right is not None:
        root_r = check_balance(tree.root.right) + 1

    return abs(root_l - root_r) <= 1


def createBinarySearchTree(arr):
    def createBst(start, end):
        if end < start:
            return
        mid = (start + end) // 2
        node = TreeNode(arr[mid])
        # print(node.data, end= ",<= data ")
        # print(start, end= ", ")
        # print(mid, end=" ,")
        # print(end)

        node.left = createBst(start, mid - 1)
        node.right = createBst(mid + 1, end)
        return node

    len_arr = len(arr)
    mid = len_arr // 2
    node = TreeNode(arr[mid])
    # print(node.data, end=", ")
    # print(mid)
    node.left = createBst(0, mid - 1)
    node.right = createBst(mid + 1, len_arr - 1)

    return Tree(node)

def BST_sequence(tree):
    def generate_sequence(node):
        if node is None:
            return []
        top = [node.data]
        left = generate_sequence(node.left)
        right = generate_sequence(node.right)

        len_left = len(left)
        len_right = len(right)
        if len_left == 0 and len_right == 0:
            return [top]

        if len_left > len_right:
            diff = len_left - len_right
            for i in range(0, diff):
                right.appen([])
        else:
            diff = len_right - len_left
            for i in range(0, diff):
                left.append([])

        result = []
        for lst in left:
            for rst in right:
                if len(lst) > 0:
                    merge = top + lst + rst
                    result.append(merge)
                if len(rst) > 0:
                    merge = top + rst + lst
                    result.append(merge)
        return result

    if tree.root is None:
        return []
    return generate_sequence(tree.root)

def test_BST_sequence():
    arr = [1,2,3,4]
    tree = createBinarySearchTree(arr)
    tree.print_pre_order()
    print('')
    result = BST_sequence(tree)
    print(result)
    print(len(result))

    arr = [5, 10, 11, 15, 19, 20, 50]
    tree = createBinarySearchTree(arr)
    tree.print_pre_order()
    print('')
    result = BST_sequence(tree)
    print(result)
    print(len(result))

    arr = [50, 20, 10, 5 , 15, 25, 60, 70, 65, 80]
    tree = createBinarySearchTree(arr)
    tree.print_pre_order()
    print('')
    result = BST_sequence(tree)
    print(result)
    print(len(result))


test_BST_sequence()

def test_BST():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = createBinarySearchTree(arr)
    tree.print_in_order()
    print('')

    result = tree.create_linked_list_at_each_depth()
    print("Link list at each level")
    for ll in result:
        ll.print_list()

    print(checkBalance(tree))

    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    tree = createBinarySearchTree(arr)
    tree.print_in_order()
    print('')
    tree.print_pre_order()
    print('')
    tree.print_post_order()
    print('')

    result = tree.create_linked_list_at_each_depth()
    print("Link list at each level")
    for ll in result:
        ll.print_list()

    print(checkBalance(tree))

#test_BST()


def test_checkBalance():

    node1 = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(3)

    node1.left = node2
    node2.left = node3

    tree = Tree(node1)
    print(checkBalance(tree))

#test_checkBalance()