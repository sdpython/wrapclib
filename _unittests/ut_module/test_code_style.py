"""
@brief      test log(time=0s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8, ExtTestCase


class TestCodeStyle(ExtTestCase):
    """Test style."""

    def test_style_src(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "wrapclib"))
        check_pep8(src_, fLOG=fLOG,
                   pylint_ignore=('C0103', 'C1801', 'R1705',
                                  'W0108', 'W0613', 'W0212'),
                   skip=["gitsrc/re2", "gitsrc\\re",
                         "gitsrc/benchlog", "gitsrc\\benchlog"])

    def test_style_test(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=fLOG, neg_pattern="temp_.*",
                   pylint_ignore=('C0103', 'C1801', 'R1705',
                                  'W0108', 'W0613', 'C0111', 'W0703',
                                  'C0116'),
                   skip=[])


if __name__ == "__main__":
    unittest.main()
