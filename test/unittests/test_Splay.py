import random
import unittest

from Splay import Splay


class TestSplay(unittest.TestCase):
    def test_insert(self):
        """Test if inserting to Splay works as expected."""
        b = Splay()

        for v in [2, 4, 5, 7, 1, -1]:
            b.insert(v)
        self.assertEqual(b.root.val, 2)
        self.assertEqual(b.root.right.val, 4)
        self.assertEqual(b.root.right.right.val, 5)
        self.assertEqual(b.root.right.right.right.val, 7)
        self.assertEqual(b.root.left.val, 1)
        self.assertEqual(b.root.left.left.val, -1)

    def test_search(self):
        b = Splay()
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
        b = Splay()
        values = random.sample(range(30), 30)
        for v in values:
            b.insert(v)

        random.shuffle(values)
        for v in values:
            self.assertEqual(b.search(v).val, v)
            b.delete(v)
            self.assertIsNone(b.search(v))
