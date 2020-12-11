import source
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.fun(3), 4)