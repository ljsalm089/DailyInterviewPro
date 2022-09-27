#!/usr/bin/env python3


__author__ = 'Jiasheng Lee'


class Node(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.val


def deepest(node):
    queue = []
    queue.append((node, 1,))
    max = queue[0]

    index: int = 0
    while index < len(queue):
        current = queue[index]
        if current[0].left:
            queue.append((current[0].left, current[1] + 1))
        if current[0].right:
            queue.append((current[0].right, current[1] + 1))
        if max[1] < current[1]:
            max = current
        index = index + 1
    return max


root = Node('a')
root.left = Node('b')
root.left.left = Node('b')
root.left.left.right = Node('c')
root.right = Node('d')

print(deepest(root))
