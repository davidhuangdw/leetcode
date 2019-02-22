from unittest import TestCase
# https://leetcode.com/problems/license-key-formatting


class LicenseKeyFormatting(TestCase):
    def licenseKeyFormatting(self, S: 'str', K: 'int') -> 'str':
        s = S.replace('-', '').upper()[::-1]
        return '-'.join(s[i:i+K] for i in range(0, len(s), K))[::-1]

    def test1(self):
        self.assertEqual("5F3Z-2E9W", self.licenseKeyFormatting("5F3Z-2e-9-w", 4))

    def test2(self):
        self.assertEqual("2-5G-3J", self.licenseKeyFormatting("2-5g-3-J", 2))
        

