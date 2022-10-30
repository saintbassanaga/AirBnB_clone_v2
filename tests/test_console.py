import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand


class MyTestCase(unittest.TestCase):
    def test_something(self):
        try:
            self.assertEqual(True, False)  # add assertion here
        except AssertionError:
            pass
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")

if __name__ == '__main__':
    unittest.main()
