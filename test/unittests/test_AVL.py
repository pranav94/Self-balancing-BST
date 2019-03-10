import random
import unittest

from AVL import AVL
from utils import preorder


class TestAVL(unittest.TestCase):
    def test_insert(self):
        """Test if inserting to AVL works as expected."""
        b = AVL()

        # Check if some values go as expected.
        for v in [2, 4, 5, 7, 1, -1]:
            b.insert(v)
        self.assertEqual(b.root.val, 4)
        self.assertEqual(b.root.left.val, 2)
        self.assertEqual(b.root.left.left.val, 1)
        self.assertEqual(b.root.left.left.left.val, -1)
        self.assertEqual(b.root.right.val, 5)
        self.assertEqual(b.root.right.right.val, 7)

        # Check if the AVL tree is balanced after each insert.
        b = AVL()
        for v in [2, 4, 5, 7, 1, -1]:
            b.insert(v)
            self.assertTrue(all(self._is_balanced(b)))

    def test_search(self):
        b = AVL()
        values = random.sample(range(30), 30)
        for v in values:
            b.insert(v)

        test_values = random.sample(range(30), 30)
        for t in test_values:
            result = b.search(t)
            if t in values:
                self.assertEqual(result.val, t)
            else:
                self.assertIsNone(result)

    def test_delete(self):
        b = AVL()
        values = random.sample(range(30), 30)
        for v in values:
            b.insert(v)

        random.shuffle(values)
        for v in values:
            self.assertEqual(b.search(v).val, v)
            b.delete(v)
            self.assertTrue(all(self._is_balanced(b)))
            self.assertIsNone(b.search(v))

    def _is_balanced(self, b):
        return [
            (-1 <= b.balance(node) <= 1)
            for node in preorder(b.root)
        ]