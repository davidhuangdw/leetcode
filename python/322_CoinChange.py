from unittest import TestCase
# https://leetcode.com/problems/coin-change
import collections


class CoinChange(TestCase):
    # O(n*m) bfs, quicker than DP
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        if not amount: return 0
        coins = sorted(c for c in set(coins) if c <= amount)
        que, done = collections.deque([(0, 0)]), set()
        while que:
            x, k = que.popleft()
            for c in coins:
                now = x+c
                if now > amount: break
                if now in done: continue
                if now == amount: return k+1
                done.add(now)
                que.append((now, k+1))
        return -1

    # # normal dp:
    # def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
    #     dp = [float("inf") for _ in range(amount+1)]
    #     dp[0] = 0
    #     for c in set(coins):
    #         for x in range(c, amount+1):
    #             dp[x] = min(dp[x], dp[x-c]+1)
    #     return -1 if dp[amount] == float("inf") else dp[amount]

    def test1(self):
        self.assertEqual(3, self.coinChange([1, 2, 5], 11))

    def test2(self):
        self.assertEqual(-1, self.coinChange([2], 3))

    def test3(self):
        self.assertEqual(0, self.coinChange([], 0))

    def test4(self):
        self.assertEqual(20, self.coinChange([186,419,83,408], 6249))


