from unittest import TestCase
# https://leetcode.com/problems/expression-add-operators/


class ExpressionAddOperators(TestCase):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        n = len(num)
        ret = []
        def dfs(i, v, last, exp):
            if i == n:
                if v+last == target: ret.append(exp)
                return
            for j in range(i+1, n+1):
                if num[i] == '0' and j-i > 1:
                    break
                cur = num[i:j]
                vcur = int(cur)

                if i == 0:
                    dfs(j, 0, vcur, cur)
                else:
                    dfs(j, v+last, vcur, exp+"+"+cur)
                    dfs(j, v+last, -vcur, exp+"-"+cur)
                    dfs(j, v, last*vcur, exp+"*"+cur)
        dfs(0, 0, 0, "")
        return ret

    def addOperators(self, num, target):
        n, res = len(num), []
        def dfs(i, sum, mul, s, exp):
            if i == n:
                if target == sum + mul*int(s): res.append(exp)
                return
            c = num[i]
            if s != "0": dfs(i+1, sum, mul, s+c, exp+c)
            mul *= int(s)
            dfs(i+1, sum, mul, c, exp+'*'+c)
            sum += mul
            dfs(i+1, sum, 1, c, exp+'+'+c)
            dfs(i+1, sum, -1, c, exp+'-'+c)
        if n: dfs(1, 0, 1, num[0], num[0])
        return res

    def test1(self):
        self.assertEqual({"1+2+3", "1*2*3"}, set(self.addOperators("123", 6)))

    def test2(self):
        self.assertEqual({"2*3+2", "2+3*2"}, set(self.addOperators("232", 8)))

    def test3(self):
        self.assertEqual({"1*0+5", "10-5"}, set(self.addOperators("105", 5)))

    def test4(self):
        self.assertEqual({"0+0", "0-0", "0*0"}, set(self.addOperators("00", 0)))

    def test5(self):
        self.assertEqual(set(), set(self.addOperators("3456237490", 9191)))


