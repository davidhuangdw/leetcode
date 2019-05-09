from unittest import TestCase
# https://leetcode.com/problems/random-pick-with-weight
import random, bisect


class RandomPickWithWeight:

    def __init__(self, w: 'List[int]'):
        sums = [w[0]]
        for v in w[1:]:
            sums.append(sums[-1]+v)
        self.sums = sums

    def pickIndex(self) -> 'int':
        x = random.randint(1, self.sums[-1])
        l, r = 0, len(self.sums)-1
        while l <= r:
            m = (l+r) >> 1
            if self.sums[m] < x:
                l = m + 1
            else:
                r = m - 1
        return l

    # def pickIndex(self) -> 'int':
    #     return bisect.bisect(self.sums, random.randint(0, self.sums[-1]-1))

# by check each one:
# class RandomPickWithWeight:
#     def __init__(self, w: 'List[int]'):
#         self.w = w
#
#     def pickIndex(self) -> 'int':
#         pre = cur = 0
#         for i, v in enumerate(self.w):
#             pre += v
#             if random.randint(1, pre) <= v: cur = i
#         return cur
