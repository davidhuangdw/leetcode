from unittest import TestCase
# https://leetcode.com/problems/trapping-rain-water/


class TrappingRainWater(TestCase):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        sum = 0
        k = 0
        for i in range(1, len(height)):
            if height[i] > height[k]:
                k = i

        mx = height[0]
        for i in range(1, k):
            if height[i] > mx:
                mx = height[i]
            else:
                sum += mx - height[i]

        mx = height[-1]
        for i in range(len(height)-2, k, -1):
            if height[i] > mx:
                mx = height[i]
            else:
                sum += mx - height[i]

        return sum

    def test1(self):
        self.assertEqual(6, self.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


