#!/usr/bin/env python3
# coding:utf-8

"""
You are given two linked-list representing two non-negative integers. The digits
are stored in reverse order and each of their nodes contain a single digit. Add
the two numbers and return it as a linked list.
"""

__author__ = 'Jiasheng Lee'


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        if l1 is None and l2 is None:
            return None
        result = None
        mod = 0
        last = None
        while True:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            tmp_result = val1 + val2 + mod
            tmp = ListNode(tmp_result % 10)
            mod = int(tmp_result / 10)
            if result is None:
                result = tmp
            else:
                last.next = tmp
            last = tmp
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is None and l2 is None and mod == 0:
                break
        return result

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(6)
l2.next.next.next = ListNode(9)

result = Solution().addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next
