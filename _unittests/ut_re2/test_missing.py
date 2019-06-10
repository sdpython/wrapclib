"""
@brief      test log(time=3s)
"""
import unittest
from pyquickhelper.pycode import ExtTestCase
from wrapclib import re2


class TestMissing(ExtTestCase):

    def test_search(self):
        m = re2.search('abc', 'abc')
        self.assertIsNotNone(m)
        self.assertEqual(m.start(), 0)

    def test_search_endpos(self):
        m = re2.search('ab', 'abc', endpos=2)
        self.assertIsNotNone(m)
        self.assertEqual(m.start(), 0)

    def test_fullmatch(self):
        m = re2.fullmatch('abc', 'abc')
        self.assertIsNotNone(m)
        self.assertEqual(m.start(), 0)

    def test_findall(self):
        m = re2.findall('ab', 'abc', endpos=2)
        self.assertIsNotNone(m)


if __name__ == "__main__":
    unittest.main()
