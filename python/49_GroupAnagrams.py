from unittest import TestCase
# https://leetcode.com/problems/group-anagrams
import collections


class GroupAnagrams(TestCase):
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        ana = collections.defaultdict(list)
        for str in strs:
            ana["".join(sorted(str))].append(str)
        return list(ana.values())

    # # by count
    # def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
    #     ana = collections.defaultdict(list)
    #     for w in strs:
    #         cnt = [0 for _ in range(26)]
    #         for ch in w:
    #             cnt[ord(ch) - ord('a')] += 1
    #         ana[tuple(cnt)].append(w)
    #     return list(ana.values())

    def test1(self):
        res = [
            ["ate","eat","tea"],
            ["nat","tan"],
            ["bat"]
        ]
        self.assertEqual(list(map(sorted, res)), list(map(sorted, self.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))))


        

