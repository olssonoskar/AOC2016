import unittest

from day01.day01 import Day01
from day02.day02 import Day02

class TestDays(unittest.TestCase):

    def test_part1(self):
        d = Day01()
        self.assertEqual(d.part1("test1_1.txt"), 12)

    def test_part2(self):
        d = Day01()
        self.assertEqual(d.part2("test1_2.txt"), 4)

    def test2_part1(self):
        d = Day02()
        self.assertEqual(d.part1("test2_1.txt"), [1,9,8,5])

    def test2_part2(self):
        d = Day02()
        self.assertEqual(d.part2("test2_1.txt"), ['5','D','B','3'])

    def test2(self):
        d = Day02()
        self.assertEqual(d.part2('../day02/input.txt'), ['8','C','B','2', '3'])

if __name__ == '__main__':
    unittest.main()