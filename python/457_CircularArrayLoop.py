from unittest import TestCase
# https://leetcode.com/problems/circular-array-loop


class CircularArrayLoop(TestCase):
    # by union_find: proof: only the root of each set has not been visited yet, so loop if x -> y and y in x's set
    def circularArrayLoop(self, nums: 'List[int]') -> 'bool':
        n = len(nums)
        parent = dict((i, i) for i in range(n))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        for i, v in enumerate(nums):
            j = (i + v) % n
            if i != j and nums[j]*nums[i] > 0:
                ri, rj = find(i), find(j)
                if ri == rj:
                    return True
                parent[ri] = rj
        return False

    # by walk-along and use set
    # def circularArrayLoop(self, nums: 'List[int]') -> 'bool':
    #     n, done = len(nums), set()
    #     for i in range(n):
    #         if i in done: continue
    #         j, cur = i, set()
    #         while j not in cur and j not in done and nums[i]*nums[j] > 0:
    #             cur.add(j)
    #             j = (j+nums[j]) % n
    #         if j in cur and nums[j] % n != 0:
    #             return True
    #         done = done.union(cur)
    #     return False

    # check by step > n:
    # def circularArrayLoop(self, nums: 'List[int]') -> 'bool':
    #     n = len(nums)
    #     for i in range(n):
    #         j, cnt = i, 0
    #         while nums[j] % n != 0 and nums[i]*nums[j] > 0 and cnt <= n:
    #             cnt += 1
    #             j = (j + nums[j]) % n
    #         if cnt > n: return True
    #     return False

    def test1(self):
        self.assertEqual(True, self.circularArrayLoop([2,-1,1,2,2]))

    def test2(self):
        self.assertEqual(False, self.circularArrayLoop([-1,2]))

    def test3(self):
        self.assertEqual(False, self.circularArrayLoop([-2,1,-1,-2,-2]))

