# Self-balancing Binary Search Trees
Implementation of several self balancing Binary Search Trees in Python with empirical analysis.

The following BSTs are implemented and analyzed accordingly.
1. Unbalanced BST
2. AVL Tree
3. Splay Tree
4. Treaps

### Developer documentation
Python version: `3.7`

No external dependencies.

### Usage

* #### BST
```python
from BST import BST

# Create
tree = BST()

# Insert
tree.insert(key)

# Search
tree.search(key) # Search

# Delete
tree.delete(key) # Delete

```

* #### AVL
```python
from AVL import AVL

# Create
tree = AVL()

# Insert
tree.insert(key)

# Search
tree.search(key) # Search

# Delete
tree.delete(key) # Delete
```

* #### Splay Tree
```python
from Splay import Splay

# Create
tree = Splay()

# Insert
tree.insert(key)

# Search
tree.search(key) # Search

# Delete
tree.delete(key) # Delete
```

* #### Treap
```python
from Treap import Treap

# Create
tree = Treap()

# Insert
tree.insert(key)

# Search
tree.search(key) # Search

# Delete
tree.delete(key) # Delete
```

### Testing
```bash
python3 -m unittest
```

### Report running times for all Tree implementations
```bash
python3 run.py
```

### Report of running times for individual Trees
```python
from report import report_BST, report_AVL, report_Splay, report_Treap
report_BST.run()
report_AVL.run()
report_Splay.run()
report_Treap.run()

```
