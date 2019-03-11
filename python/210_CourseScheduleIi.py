from unittest import TestCase
# https://leetcode.com/problems/course-schedule-ii
import collections


class CourseScheduleIi(TestCase):
    def findOrder(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
        n = numCourses
        deg, e = [0 for _ in range(n)], [[] for _ in range(n)]
        for a, b in prerequisites:
            e[b].append(a)
            deg[a] += 1
        leaves = collections.deque(u for u in range(n) if not deg[u])
        path = []
        while leaves:
            u = leaves.popleft()
            path.append(u)
            for v in e[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    leaves.append(v)
        return path if len(path) == n else []

    # # dfs
    # def findOrder(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
    #     n = numCourses
    #     e = [[] for _ in range(n)]
    #     for a, b in prerequisites:
    #         e[a].append(b)
    #
    #     def dfs_cycle(u):
    #         done.add(u)
    #         parents.add(u)
    #         for v in e[u]:
    #             if v in parents: return True
    #             if v in done: continue
    #             if dfs_cycle(v): return True
    #         parents.remove(u)
    #         path.append(u)
    #
    #     path, done = [], set()
    #     for i in range(n):
    #         if i in done: continue
    #         parents = set()
    #         if dfs_cycle(i): return []
    #     return path

    def test1(self):
        self.assertEqual([0,1], self.findOrder(2, [[1,0]]))

    def test2(self):
        self.assertEqual([0,1,2,3], self.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))

