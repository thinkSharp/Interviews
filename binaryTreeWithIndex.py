import random

class TreeNode:
    def __init__(self, data, index):
        self.data = data
        self.index = index
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root, count):
        self.root = root
        self.count = count
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

    def getRandomNode(self):
        def getChildRandom(node, rand):
            if node is None:
                return None
            if node.index == rand:
                return node.data
            elif node.index > rand:
                return getChildRandom(node.left, rand)
            else:
                return getChildRandom(node.right, rand)

        if self.root is None:
            return None

        number = random.randint(0, self.count)
        return getChildRandom(self.root, number)

    def getPathsWithSum(self, sum):
        def getNodeSum(child, running_sum):
            if child is None:
                return 0
            paths = 0
            current_sum = running_sum + child.data
            if current_sum == sum:
                paths += 1
            if current_sum > sum:
                return paths

            paths += getNodeSum(child.left, current_sum)
            paths += getNodeSum(child.right, current_sum)

            return paths

        def getSumNodeFromChild(child):
            if child is None:
                return 0

            root_path = getNodeSum(child, 0)
            left_paths = getSumNodeFromChild(child.left)
            right_paths = getSumNodeFromChild(child.right)

            return root_path + left_paths + right_paths

        if self.root is None:
            return None

        return getSumNodeFromChild(self.root)


def createBinarySearchTree(arr):
    def create_bst(arr, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        node = TreeNode(arr[mid], mid)
        node.left = create_bst(arr, start, mid - 1)
        node.right = create_bst(arr, mid + 1, end)

        return node

    root_mid = len(arr) // 2
    root_node = TreeNode(arr[root_mid], root_mid)
    tree = Tree(root_node, len(arr) - 1)
    root_node.left = create_bst(arr, 0 , root_mid - 1)
    root_node.right = create_bst(arr, root_mid + 1, len(arr) -1)

    return tree

def test_create_binary_tree():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = createBinarySearchTree(arr)
    tree.print_pre_order()
    print('')

    print(tree.getRandomNode())
    print(tree.getRandomNode())
    print(tree.getRandomNode())
    print(tree.getRandomNode())
    print(tree.getRandomNode())

    arr = [1, 2, 3, 4, 5, 6]
    tree = createBinarySearchTree(arr)
    tree.print_pre_order()
    print('')

    print(tree.getPathsWithSum(4))

test_create_binary_tree()