from unittest import TestCase
# https://leetcode.com/problems/container-with-most-water


class ContainerWithMostWater(TestCase):
    def maxArea(self, height: 'List[int]') -> 'int':
        l, r, res = float("inf"), float("-inf"), 0
        for h, i in sorted(((h, i) for i, h in enumerate(height)), reverse=True):
            l = min(i, l)
            r = max(i, r)
            res = max(res, (r-l)*h)
        return res

    # # two pointer O(n):
    # # proof of the safe elimination:
    # # (i, j) means we are going to get the max area from the range i to j
    # # 1. case hi <= hj:
    # #   * we can prove that j is the best choice(within the range from i to j) for i
    # #   * for any k(i < k < j):
    # #     area(i, j) == min(hi, hj)*(j-i) == hi*(j-i) > hi*(k-i) >= min(hi,hk)*(k-i) == area(i, k)
    # #     area(i, j) > area(i, k)
    # #   * it means j is the best choice for i, so i can be safely eliminated
    # #     * max_area_of_range(i, j) == max(max_area_of_range(i+1, j), area(i, j))
    # # 2. case hi >= hj:(i, j) means we are going to get the max area from the range i to j:
    # #   * similarly, we can prove that i is the best choice(within the range from i to j) for j
    # #   * so we can safely eliminate j
    # #     * max_area_of_range(i, j) == max(max_area_of_range(i+1, j), area(i, j))
    # def maxArea(self, height: 'List[int]') -> 'int':
    #     i, j, res = 0, len(height)-1, 0
    #     while i < j:
    #         if height[i] <= height[j]:
    #             res = max(res, height[i]*(j-i))
    #             i += 1
    #         else:
    #             res = max(res, height[j]*(j-i))
    #             j -= 1
    #     return res

    def test1(self):
        self.assertEqual(49, self.maxArea([1,8,6,2,5,4,8,3,7]))

