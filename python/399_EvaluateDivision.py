from unittest import TestCase
# https://leetcode.com/problems/evaluate-division


class EvaluateDivision(TestCase):
    def calcEquation(self, equations: 'List[List[str]]', values: 'List[float]', queries: 'List[List[str]]') -> 'List[float]':
        parent = {}

        def root(a):
            if a in parent:
                p, ma = parent[a]
                if p != a:
                    r, m = root(p)
                    parent[a] = (r, m*ma)
            else:
                parent[a] = (a, 1.0)
            return parent[a]
        for i, (a,b) in enumerate(equations):
            ra, ma = root(a)
            rb, mb = root(b)
            if ra != rb:
                parent[ra] = (rb, mb*values[i]/ma)

        res = []
        for a, b in queries:
            if a not in parent or b not in parent:
                res.append(-1.0)
            else:
                ra, ma = root(a)
                rb, mb = root(b)
                res.append(ma/mb if ra == rb else -1.0)
        return res

    def test1(self):
        self.assertEqual([6.0, 0.5, -1.0, 1.0, -1.0 ],
                         self.calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]))




        

