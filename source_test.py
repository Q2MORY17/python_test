import source
import roboclaw_bareminimum
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.fun(3), 4)

    def test2(self):
        self.assertEqual(roboclaw_bareminimum.rc.Open(), 0)