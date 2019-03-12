from unittest import TestCase
# https://leetcode.com/problems/exclusive-time-of-functions


class ExclusiveTimeOfFunctions(TestCase):
    def exclusiveTime(self, n: 'int', logs: 'List[str]') -> 'List[int]':
        st, pre, res = [], 0, [0 for _ in range(n)]
        for log in logs:
            i, op, t = log.split(':')
            start = op[0] == 's'
            t = int(t) if start else int(t)+1
            if st:
                res[st[-1]] += t-pre
            if start:
                st.append(int(i))
            else:
                st.pop()
            pre = t
        return res

    def test1(self):
        logs = ["0:start:0",
                "1:start:2",
                "1:end:5",
                "0:end:6"]
        self.assertEqual([3,4], self.exclusiveTime(2, logs))

        

