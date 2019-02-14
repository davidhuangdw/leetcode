from unittest import TestCase
# https://leetcode.com/problems/sliding-puzzle/
import collections


class SlidingPuzzle:
    def __init__(self):
        steps = dict()
        que = collections.deque()
        que.appendleft((0, (1, 2, 3, 4, 5, 0)))
        while que:
            cnt, state = que.pop()
            steps[state] = cnt
            i = state.index(0)
            outbound = {2, 3}
            for df in (1, -1, 3, -3):
                j = i+df
                if not (0 <= j < 6 and {i, j} != outbound): continue
                arr = list(state)
                arr[i], arr[j] = arr[j], arr[i]
                next_state = tuple(arr)
                if next_state in steps: continue
                que.appendleft((cnt+1, next_state))
        self.steps = steps

    def slidingPuzzle(self, board: 'List[List[int]]') -> 'int':
        state = tuple(board[0]+board[1])
        return self.steps.get(state, -1)


class Tests(TestCase):
    def test1(self):
        s = SlidingPuzzle()
        self.assertEqual(1, s.slidingPuzzle([[1, 2, 3], [4, 0, 5]]))

    def test2(self):
        s = SlidingPuzzle()
        self.assertEqual(-1, s.slidingPuzzle([[1,2,3],[5,4,0]]))

    def test3(self):
        s = SlidingPuzzle()
        self.assertEqual(5, s.slidingPuzzle([[4,1,2],[5,0,3]]))

