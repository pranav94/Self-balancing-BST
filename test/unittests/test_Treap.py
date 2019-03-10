import random
import unittest

from Treap import Treap


class TestTreap(unittest.TestCase):
    def test_insert(self):
        """Test if inserting to Treap works as expected."""
        b = Treap()

        for v in random.sample(range(30), 30):
            b.insert(v)


    def test_search(self):
        b = Treap()
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
        b = Treap()
        values = random.sample(range(30), 30)
        for v in values:
            b.insert(v)

        random.shuffle(values)

        for v in values:
            self.assertEqual(b.search(v).val, v)
            b.delete(v)
            self.assertIsNone(b.search(v))
