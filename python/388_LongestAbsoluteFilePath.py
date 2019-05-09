from unittest import TestCase
# https://leetcode.com/problems/longest-absolute-file-path/
import collections


class LongestAbsoluteFilePath(TestCase):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        ret = 0
        lines = input.split("\n")
        sums = [0]
        for line in lines:
            line = line.split("\t")
            k, name = len(line), line[-1]
            sum = sums[k-1] + len(name) + 1
            if "." in name:
                ret = max(ret, sum-1)
            if k < len(sums):
                sums[k] = sum
            else:
                sums.append(sum)
        return ret


    def lengthLongestPath(self, input):
        nest, ret = [], 0
        for line in input.split("\n"):
            d = 0
            while line[d] == "\t":
                d += 1
            if d >= len(nest): nest.append(0)
            nest[d] = (nest[d-1]+1 if d else 0) + len(line) - d
            if "." in line:
                ret = max(ret, nest[d])
        return ret


    def test1(self):
        self.assertEqual(32, self.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
