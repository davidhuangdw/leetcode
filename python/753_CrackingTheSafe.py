from unittest import TestCase
# https://leetcode.com/problems/cracking-the-safe


class CrackingTheSafe(TestCase):
    def crackSafe(self, n: 'int', k: 'int') -> 'str':
        done, path, digits = set(), [], list("0123456789")

        def euler(pre):
            for d in digits[:k]:
                cur = pre + d
                if cur not in done:
                    done.add(cur)
                    euler(cur[1:])
                    path.append(d)
        pre = "0"*(n-1)
        euler(pre)
        return "".join(path + list(pre))

    def test1(self):
        self.assertEqual("01100", self.crackSafe(2, 2))


