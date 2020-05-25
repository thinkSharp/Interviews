# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
goal: serialize and deserialize for binary tree
ideas:
    in order to serialize into array, I am going to use following formula
    root, left, right, lf,lr, rl,rr
    left = root_index * 2 + 1
    right = left + 1
    to serialize:
       recursively as well
       in order 
       root, left, right

    to deserialize:
       read from the begining of the list
       recursively build the children

'''


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def child_serialize(node, index, result):
            if node is None:
                return None

            left_index = index * 2 + 1
            right_index = left_index + 1

            new_spaces = right_index + 1 - len(result)
            if new_spaces > 0:
                result += [None] * new_spaces

            left_val = node.left.val if node.left else None
            right_val = node.right.val if node.right else None
            result[left_index] = left_val
            result[right_index] = right_val

            if node.left:
                child_serialize(node.left, left_index, result)

            if node.right:
                child_serialize(node.right, right_index, result)

        if root is None:
            return []

        res = [root.val, None]

        child_serialize(root, 0, res)

        while res[-1] is None:
            res.pop()

        print(res)
        print(root)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        len_data = len(data)

        def deserialize_child(node, index):
            left_index = index * 2 + 1
            right_index = left_index + 1

            if index >= len_data or left_index >= len_data:
                return
            print("node:{3},index:{0}, left:{1}, right:{2}".format(index, left_index, right_index, node.val))
            if data[left_index] is not None:
                lnode = TreeNode(data[left_index])
                node.left = lnode
                deserialize_child(lnode, left_index)

            if right_index < len_data and data[right_index] is not None:
                rnode = TreeNode(data[right_index])
                node.right = rnode
                deserialize_child(rnode, right_index)

        if len_data == 0:
            return None

        root = TreeNode(data[0])
        deserialize_child(root, 0)
        print(root)
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

def test_codec():
    root = TreeNode(1)
    lr = TreeNode(2)
    rr = TreeNode(3)
    root.left = lr
    root.right =rr
    lll = TreeNode(1)
    llr = TreeNode(3)
    lr.left = lll
    lr.right = llr
    rrl = TreeNode(2)
    rrr = TreeNode(4)
    rr.left = rrl
    rr.right = rrr
    print(root)
    c = Codec()
    val = c.serialize(root)
    print(val)
    root2 = c.deserialize(val)
    print(root2)

test_codec()

a = [0]
print(len(a))
print(hex(id(a)))

a += [0] * 4
print(len(a))
print(hex(id(a)))

import functools
a = [1,2,3,4,5]
b = {}

b[(1,2)] = 3
print(b)