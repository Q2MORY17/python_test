import roboclaw_bareminimum
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(roboclaw_bareminimum.rc.Open(), 1)