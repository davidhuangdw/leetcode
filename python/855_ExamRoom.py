from unittest import TestCase
# https://leetcode.com/problems/exam-room
import bisect, heapq


class ExamRoom:
    def __init__(self, N: 'int'):
        self.n = N
        self.seats = []

    def seat(self) -> 'int':
        n, seats = self.n, self.seats
        if not seats:
            p = 0
        else:
            mx, p = seats[0], 0
            for x, y in zip(seats, seats[1:]):
                dis = (y-x) >> 1
                if dis > mx:
                    mx, p = dis, x+dis
            dis = n - 1 - seats[-1]
            if dis > mx: p = n-1
        bisect.insort(seats, p)
        return p

    def leave(self, p: 'int') -> 'None':
        self.seats.remove(p)

    # # by heap: O(logn) for both seat() and leave()
    # def __init__(self, N: 'int'):
    #     self.que = []
    #     self.n = N
    #     self.left = {}
    #     self.right = {}
    #     self.put(-1, N)
    #
    # def put(self, a, b):
    #     que, n = self.que, self.n
    #     dis = b if a == -1 else (n-1-a if b == n else (b-a)>>1)
    #     seg = [-dis, a, b, True]
    #     self.left[b] = seg
    #     self.right[a] = seg
    #     heapq.heappush(que, seg)
    #
    # def seat(self) -> 'int':
    #     que, n = self.que, self.n
    #     while not que[0][-1]:
    #         heapq.heappop(que)
    #     _, a, b, _ = heapq.heappop(que)
    #     p = 0 if a == -1 else (n-1 if b == n else (a+b)>>1)
    #     self.put(a, p)
    #     self.put(p, b)
    #     return p
    #
    # def leave(self, p: 'int') -> 'None':
    #     l = self.left[p]
    #     r = self.right[p]
    #     l[-1] = False
    #     r[-1] = False
    #     self.put(l[1], r[2])


class ExamRoomTests(TestCase):
    def test1(self):
        r = ExamRoom(10)
        self.assertEqual(0, r.seat())
        self.assertEqual(9, r.seat())
        self.assertEqual(4, r.seat())
        self.assertEqual(2, r.seat())
        r.leave(4)
        self.assertEqual(5, r.seat())


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)

