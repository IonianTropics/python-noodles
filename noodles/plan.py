"""
Generating a binary factor tree
"""

from bintree import Node

q = Node(2162160)

q.factor()
q.right = Node(10)
q.right.left = Node(11)
q.printtree()

