from unittest import TestCase
# https://leetcode.com/problems/online-election
import collections, bisect


class TopVotedCandidate:
    def __init__(self, persons: 'List[int]', times: 'List[int]'):
        self.winners, self.times = [], []
        mx, votes = -1, collections.Counter()
        for p, t in zip(persons, times):
            votes[p] += 1
            if votes[p] >= votes[mx] and p != mx:
                mx = p
                self.times.append(t)
                self.winners.append(p)

    def q(self, t: 'int') -> 'int':
        return self.winners[bisect.bisect_right(self.times, t)-1]


class TopVotedCandidateTests(TestCase):
    def test1(self):
        v = TopVotedCandidate([0,1,1,0,0,1,0],[0,5,10,15,20,25,30])
        self.assertEqual(0, v.q(3))
        self.assertEqual(1, v.q(12))
        self.assertEqual(1, v.q(25))
        self.assertEqual(0, v.q(15))
        self.assertEqual(0, v.q(24))
        self.assertEqual(1, v.q(8))


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

