from unittest import TestCase
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


class BestTimetoBuyandSellStockwithCooldown(TestCase):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        canBuy, bought, sold = 0, float("-inf"), 0
        for v in prices:
            canBuy, bought, sold = max(canBuy, sold), max(bought, canBuy-v), max(sold, bought+v)
        return sold

    def test1(self):
        self.assertEqual(3, self.maxProfit([1,2,3,0,2]))