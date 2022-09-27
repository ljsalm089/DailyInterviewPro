#!/usr/bin/env python3
"""
check if a tree is a binary search tree.
"""

__author__ = 'Jiasheng Lee'


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_bst(tree: Node):
    left_success = (tree.value >= tree.left.value) if tree.left else True
    right_success = (tree.value <= tree.right.value) if tree.right else True
    return left_success and right_success\
        and (is_bst(tree.left) if tree.left else True)\
        and (is_bst(tree.right) if tree.right else True)


a = Node(5)
a.left = Node(3)
a.right = Node(6)
a.left.left = Node(1)
a.left.right = Node(4)
a.right.left = Node(7)
print(is_bst(a))
