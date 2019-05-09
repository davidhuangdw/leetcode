from unittest import TestCase
# https://leetcode.com/problems/decode-string


class DecodeString(TestCase):
    def decodeString(self, s: 'str') -> 'str':
        n = len(s)

        def dec(i):
            pre, res = None, []
            while i < n and s[i] != ']':
                ch = s[i]
                if ch == '[':
                    num = int(s[pre:i])
                    sub, i = dec(i+1)
                    res += num*sub
                    pre = None
                elif not ch.isdigit():
                    res.append(ch)
                elif pre is None:
                    pre = i
                i += 1
            return res, i
        return "".join(dec(0)[0])

    # # iter
    # def decodeString(self, s: 'str') -> 'str':
    #     st, parts, digits = [], [], []
    #     for c in s:
    #         if c.isdigit():
    #             digits.append(c)
    #         elif c == '[':
    #             k = int("".join(digits))
    #             digits = []
    #             st.append(parts)
    #             st.append(k)
    #             parts = []
    #         elif c == ']':
    #             str = "".join(parts)
    #             k = st.pop()
    #             parts = st.pop()
    #             parts.append(k*str)
    #         else:
    #             parts.append(c)
    #     return "".join(parts)


    def test1(self):
        self.assertEqual("aaabcbc", self.decodeString("3[a]2[bc]"))

    def test2(self):
        self.assertEqual("accaccacc", self.decodeString("3[a2[c]]"))

    def test3(self):
        self.assertEqual("abcabccdcdcdef", self.decodeString("2[abc]3[cd]ef"))

