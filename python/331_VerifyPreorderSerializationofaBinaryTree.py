from unittest import TestCase
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/


class VerifyPreorderSerializationofaBinaryTree(TestCase):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        df = 1
        for s in preorder.split(","):
            if df == 0: return False
            df += -1 if s == "#" else 1
        return df == 0

    def test1(self):
        self.assertEqual(True, self.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))

    def test2(self):
        self.assertEqual(False, self.isValidSerialization("1,#"))

    def test3(self):
        self.assertEqual(False, self.isValidSerialization("9,#,#,1,#,#"))

    def test4(self):
        self.assertEqual(False, self.isValidSerialization(""))

    def test5(self):
        self.assertEqual(True, self.isValidSerialization("#"))
