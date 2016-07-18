import unittest 

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            n = Node(data)
            self.root = n
        else:
            cursor = self.root
            prev = None
            while(cursor != None):
                if data < cursor.data:
                    prev = cursor
                    cursor = cursor.left
                elif data >= cursor.data:
                    prev = cursor
                    cursor = cursor.right
            if data < prev.data:
                n = Node(data)
                prev.left = n
            elif data >= prev.data:
                n = Node(data)
                prev.right = n
        return self

    def inorder_traversal(self, n=self.root):
        if n == None:
            print self
        inorder_traversal(n.left)
        print n.data
        inorder_traversal(n.right)



class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.BT = BinaryTree()

    def test_insert_empty(self):
        self.BT.insert(1)
        self.assertEqual(self.BT.root.data, 1)

    def test_insert_many(self):
        self.BT.insert(5)
        self.BT.insert(3)
        self.BT.insert(7)

        self.BT.insert(2)
        self.BT.insert(4)

        self.BT.insert(6)
        self.BT.insert(8)

        left_subtree = self.BT.root.left
        right_subtree = self.BT.root.right

        self.assertEqual(self.BT.root.data, 5)
        self.assertEqual(left_subtree.data, 3)
        self.assertEqual(right_subtree.data, 7)

        self.assertEqual(left_subtree.left.data, 2)
        self.assertEqual(left_subtree.right.data, 4)
        self.assertEqual(right_subtree.left.data, 6)
        self.assertEqual(right_subtree.right.data, 8)

    def test_inorder_traversal(self):
        self.BT.insert(5)
        self.BT.insert(3)
        self.BT.insert(7)

        self.BT.insert(2)
        self.BT.insert(4)

        self.BT.insert(6)
        self.BT.insert(8)

        self.assertEqual(self.BT.inorder_traversal(), [2,3,4,5,6,7,8])

if __name__ == '__main__':
    unittest.main()
