import time
import random
from collections import OrderedDict

from Treap import Treap


def randomized():
    print("#########################")
    print("Random distribution of data")
    print("#########################")
    operations = OrderedDict({
        "Insert": lambda b, x: b.insert(x),
        "Search": lambda b, x: b.search(x),
        "Delete": lambda b, x: b.delete(x),
    })
    for n in range(1000, 100001, 2000):
        b = Treap()
        for name in operations:
            start = time.time()
            op = operations[name]
            for i in random.sample(range(0, n), n):
                op(b, i)
            elapsed = time.time() - start
            print('{},{},{}'.format(name, n, round(1000 * elapsed, 4)))


def recurring():
    print("#########################")
    print("Recurring data")
    print("#########################")
    for n in range(1000, 100000, 2000):
        b = Treap()
        for i in random.sample(range(0, n), n):
            b.insert(i)
        start = time.time()
        for i in [random.randint(400, 405) for _ in range(n)]:
            b.search(i)

        elapsed = time.time() - start
        print('{}'.format(round(1000 * elapsed, 4)))


def sequential():
    print("#########################")
    print("Sequential data")
    print("#########################")
    operations = OrderedDict({
        "Insert": lambda b, x: b.insert(x),
        "Search": lambda b, x: b.search(x),
        "Delete": lambda b, x: b.delete(x),
    })
    for n in range(10, 1001, 20):
        b = Treap()
        for name in operations:
            op = operations[name]
            values = list(range(n))
            if name == "Delete":
                values.reverse()
            start = time.time()
            for i in values:
                op(b, i)
            elapsed = time.time() - start
            print('{},{},{}'.format(name, n, round(1000 * elapsed, 4)))


def run():
    print("** Treap **")
    randomized()
    recurring()
    sequential()