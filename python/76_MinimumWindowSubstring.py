from unittest import TestCase
# https://leetcode.com/problems/minimum-window-substring
import collections


class MinimumWindowSubstring(TestCase):
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        t_mores = collections.Counter(t)
        missing, n, j, res = len(t_mores), len(s), 0, (float("inf"), 0, 0)
        for i in range(n):
            while j < n and missing:
                t_mores[s[j]] -= 1
                missing -= t_mores[s[j]] == 0
                j += 1
            if not missing:
                res = min(res, (j-i, i, j))
            t_mores[s[i]] += 1
            missing += t_mores[s[i]] > 0
        return s[res[1]:res[2]]

    # better: iterate j(right end)
    # def minWindow(self, s: 'str', t: 'str') -> 'str':
    #     if not t: return ""
    #     t_mores = collections.Counter(t)         # t_count - s_count
    #     missing, i, res = len(t_mores), 0, (float("inf"), 0, 0)
    #     for j, cj in enumerate(s):
    #         t_mores[cj] -= 1
    #         missing -= t_mores[cj] == 0
    #         if missing: continue
    #         while not missing:
    #             t_mores[s[i]] += 1
    #             missing += t_mores[s[i]] > 0
    #             i += 1
    #         res = min(res, (j-i, i-1, j+1))
    #     return s[res[1]:res[2]]

    # pre-process filter:
    # def minWindow(self, s: 'str', t: 'str') -> 'str':
    #     if not t: return ""
    #     t_mores = collections.Counter(t)
    #     filtered = [(i, c) for i, c in enumerate(s) if c in t_mores]
    #     missing, fi, res = len(t_mores), 0, (float("inf"), 0, 0)
    #     for j, cj in filtered:
    #         t_mores[cj] -= 1
    #         missing -= t_mores[cj] == 0
    #         if missing: continue
    #         while not missing:
    #             i, ci = filtered[fi]
    #             t_mores[ci] += 1
    #             missing += t_mores[ci] > 0
    #             fi += 1
    #         res = min(res, (j-i, i, j+1))
    #     return s[res[1]:res[2]]

    def test1(self):
        self.assertEqual("BANC", self.minWindow("ADOBECODEBANC", "ABC"))


        

