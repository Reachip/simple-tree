from random import randint
from tree import binarytree as bt 

tree = bt.Node(10)
[tree.insert(randint(0, 700)) for i in range(10)]

tree.print_tree()

if tree.find(10):
    print("\n10 found in the tree.")

# 10  15  236  60  132  335  310  669  519  569  693  
# 10 found in the tree.

