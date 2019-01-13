from unittest import TestCase
# https://leetcode.com/problems/super-ugly-number/
import heapq


class SuperUglyNumber(TestCase):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # concise by generator & heap.merge
        nums = [1]

        def gen(p):
            for num in nums:
                yield num*p
        heap = heapq.merge(*map(gen, primes))
        while len(nums) < n:
            num = next(heap)
            if num > nums[-1]:
                nums.append(num)
        return nums[-1]

    def nthSuperUglyNumber1(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heads = [0] * len(primes)
        nums = [1]
        heap = []
        def next(i):
            return nums[heads[i]]*primes[i]
        for i in range(len(primes)):
            heapq.heappush(heap, (next(i), i))
        while len(nums) < n:
            nxt, i = heapq.heappop(heap)
            if nxt > nums[-1]:
                nums.append(nxt)
            heads[i] += 1
            heapq.heappush(heap, (next(i), i))
        return nums[-1]

    def test1(self):
        self.assertEqual(1, self.nthSuperUglyNumber(1, [2,3,5]))

    def test2(self):
        self.assertEqual(32, self.nthSuperUglyNumber(12, [2,7,13,19]))
