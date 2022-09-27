#!/usr/bin/env python3


__author__ = 'Jiasheng Lee'


class Solution(object):

    def buddyStrings(self, a, b):
        if len(a) != len(b):
            return False

        positions = []
        for index in range(0, len(a)):
            if a[index] != b[index]:
                if len(positions) >= 2:
                    return False
                else:
                    positions.append(index)
        return len(positions) == 2 and a[positions[0]] == b[positions[1]]\
            and a[positions[1]] == b[positions[0]]


print(Solution().buddyStrings('aaaaaabc', 'aaaaaacb'))
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
print(Solution().buddyStrings('aaaaaab', 'aaaaaaacb'))
print(Solution().buddyStrings('baaaaac', 'caaaaab'))
