from unittest import TestCase
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
import collections


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

    # general solution: for at least k days cooldown
    # def maxProfit(self, prices):
    #     # buy[i] = sell_max[i-1-K] - prices[i]
    #     # sell[i] = buy_max[i-1] + prices[i]
    #     K = 1           # at least K days cooldown
    #     K += 1          # since need to keep the values of last K+1 days
    #     que = collections.deque()       # latest (maxBuy, maxSell) pairs
    #     que.append((float("-inf"), 0))
    #     for v in prices:
    #         buy_max = max(que[-1][0],
    #                       (que[0][1] if len(que) == K else 0) - v)
    #         sell_max = max(que[-1][1], que[-1][0] + v)
    #         que.append((buy_max, sell_max))
    #         if len(que) > K:
    #             que.popleft()
    #     return que[-1][1]

    def test1(self):
        self.assertEqual(3, self.maxProfit([1,2,3,0,2]))