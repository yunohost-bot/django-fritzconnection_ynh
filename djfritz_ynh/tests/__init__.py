import os
import unittest.util

from bx_py_utils.test_utils.deny_requests import deny_any_real_request


# Hacky way to expand the failed test output:
unittest.util._MAX_LENGTH = os.environ.get('UNITTEST_MAX_LENGTH', 300)


# Deny any real internet connection:
deny_any_real_request()
