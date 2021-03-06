from __future__ import unicode_literals

import os
import unittest
from pathlib import Path

from pylint.lint import Run

ROOT_PATH = Path(__file__).parent

RCFILEPATH = ROOT_PATH / "tools" / "pylintrc"

TESTED_PACKAGES = ["snips_nlu", "snips_nlu_samples", "debug"]


class TestLinting(unittest.TestCase):
    def test_linting(self):
        args = ["--output-format", "parseable", "--rcfile", str(RCFILEPATH)]
        args += all_python_files()

        run = Run(args, exit=False)
        self.assertEqual(0, run.linter.msg_status)


def all_python_files():
    files = []
    for p in TESTED_PACKAGES:
        for dirpath, _, filenames in os.walk(str(ROOT_PATH / p)):
            files += [
                os.sep.join([dirpath, f])
                for f in filenames if f.endswith(".py")
            ]

    return files
