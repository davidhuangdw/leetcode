from unittest import TestCase
# https://leetcode.com/problems/reconstruct-itinerary/
import collections


class ReconstructItinerary(TestCase):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tos = collections.defaultdict(list)
        for fr, to in sorted(tickets)[::-1]:
            tos[fr].append(to)
        ret = []

        def dfs(fr):
            while tos[fr]:
                dfs(tos[fr].pop())
            ret.append(fr)
        dfs("JFK")
        return ret[::-1]

    def test1(self):
        self.assertEqual(["JFK", "MUC", "LHR", "SFO", "SJC"], self.findItinerary(
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        ))

    def test2(self):
        self.assertEqual(["JFK","ATL","JFK","SFO","ATL","SFO"], self.findItinerary(
            [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
        ))

    def test3(self):
        self.assertEqual(["JFK","NRT","JFK","KUL"], self.findItinerary(
            [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
        ))
