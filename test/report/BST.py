import time
import unittest
import random

from BST import BST


class Base(unittest.TestCase):
    def setUp(self):
        self._started_at = time.time()
        self.b = BST()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        operation, values = self.shortDescription().split(",")
        print('{operation},{},{}ms'.format(
            values, round(1000*elapsed, 4), operation=operation))


class TestSearch(Base):
    def setUp(self):
        super().setUp()
        self.BIG_BST = BST()

    def test_get_10_from_bst(self):
        """Search,10"""
        self.b = self.BIG_BST
        for i in random.sample(range(0, 10), 10):
            self.b.search(i)


class TestSet(Base):
    def setUp(self):
        super().setUp()
        self.b = BST()

    def test_insert_10_into_bst(self):
        """Insert,10"""
        for i in random.sample(range(0, 10), 10):
            self.b.insert(i)


class Testdelete(Base):
    def setUp(self):
        super().setUp()
        self.BIG_BST = BST()

    def test_delete_10_from_bst(self):
        """delete,10"""
        self.b = self.BIG_BST
        for i in random.sample(range(0, 10), 10):
            self.b.delete(i)
