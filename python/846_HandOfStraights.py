from unittest import TestCase
# https://leetcode.com/problems/hand-of-straights
import heapq,collections


class HandOfStraights(TestCase):
    def isNStraightHand(self, hand: 'List[int]', W: 'int') -> 'bool':
        n = len(hand)
        if n % W: return False
        heapq.heapify(hand)
        count = collections.Counter(hand)
        while hand:
            i = heapq.heappop(hand)
            if count[i] == 0: continue
            count[i] -= 1
            for j in range(i+1, i+W):
                if count[j] == 0:
                    return False
                count[j] -= 1
        return True

    # # sort first: O(mlogm + min(m*w,n))
    # def isNStraightHand(self, hand: 'List[int]', W: 'int') -> 'bool':
    #     n = len(hand)
    #     if n % W: return False
    #     count = collections.Counter(hand)
    #     for i in sorted(count):
    #         if not count[i]: continue
    #         for j in range(i+1, i+W):
    #             if count[j] < count[i]:
    #                 return False
    #             count[j] -= count[i]
    #     return True

    # # O(mlogm): condensed info -- how many unfinished
    # def isNStraightHand(self, hand: 'List[int]', W: 'int') -> 'bool':
    #     n = len(hand)
    #     if n % W: return False
    #     count = collections.Counter(hand)
    #     opened, pre, starts = 0, 0, collections.deque()
    #     for i in sorted(count):
    #         if count[i] < opened or (opened and i > pre+1):
    #             return False
    #         starts.append(count[i] - opened)
    #         pre, opened = i, count[i]
    #         if len(starts) == W: opened -= starts.popleft()
    #     return not opened

    def test1(self):
        self.assertEqual(True, self.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))

    def test2(self):
        self.assertEqual(False, self.isNStraightHand([1,2,3,6,2,3,4,7,8], 4))

    def test3(self):
        self.assertEqual(False, self.isNStraightHand([1,5], 2))

