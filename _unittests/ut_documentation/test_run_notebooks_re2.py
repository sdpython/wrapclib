# -*- coding: utf-8 -*-
"""
@brief      test log(time=25s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
import wrapclib


class TestRunNotebooksRe2(ExtTestCase):

    def test_run_re2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import jyquickhelper as jyq  # pylint: disable=C0415
        self.assertNotEmpty(jyq)
        self.assertNotEmpty(wrapclib)

        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks")
        test_notebook_execution_coverage(__file__, "re2", folder,
                                         this_module_name='wrapclib', fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
