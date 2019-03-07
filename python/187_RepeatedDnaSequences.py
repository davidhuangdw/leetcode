from unittest import TestCase
# https://leetcode.com/problems/repeated-dna-sequences


class RepeatedDnaSequences(TestCase):
    def findRepeatedDnaSequences(self, s: 'str') -> 'List[str]':
        code = {c:i for i, c in enumerate("ACGT")}
        mask, cnt, i, cur, res = (1 << 20) -1, {}, 0, 0, []
        for j, c in enumerate(s):
            cur = (cur << 2) + code[c]
            if j < 9: continue
            cur = cur & mask
            cnt[cur] = cnt.get(cur, 0)+1
            if cnt[cur] == 2:
                res.append(s[j-9:j+1])
        return res

    def test1(self):
        self.assertEqual(["AAAAACCCCC", "CCCCCAAAAA"], self.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

