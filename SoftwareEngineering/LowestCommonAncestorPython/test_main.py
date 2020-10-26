import unittest
import main
from main import Node

class TestMain(unittest.TestCase):

    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)

    def tearDown(self):
        pass

    def test_findPath(self):
        self.assertTrue(main.findPath(None, None, None))
        self.assertTrue(main.findPath(self.root, 4, 5))
        self.assertFalse(main.findPath(self.root, 4, 8))
        self.assertTrue(main.findPath(self.root, 4, 4))
        self.assertFalse(main.findPath(self.root, 4, None))
        self.assertFalse(main.findPath(self.root, None, 5))
        self.assertTrue(main.findPath(self.root, 4, 7))
        self.assertTrue(main.findPath(self.root, 1, 7))
        self.assertTrue(main.findPath(self.root, 7, 1))

    def test_findLCA(self):
        self.assertEqual(main.findLCA(None, None, None), None)
        self.assertEqual(main.findLCA(self.root, 2, None), None)
        self.assertEqual(main.findLCA(self.root, None, 4), None)
        self.assertEqual(main.findLCA(self.root, 2, 4), 2)
        self.assertEqual(main.findLCA(self.root, 4, 5), 2)
        self.assertEqual(main.findLCA(self.root, 4, 6), 1)
        self.assertEqual(main.findLCA(self.root, 3, 4), 1)
        self.assertEqual(main.findLCA(self.root, 2, 4), 2)


if __name__ == '__main__':
    unittest.main()

