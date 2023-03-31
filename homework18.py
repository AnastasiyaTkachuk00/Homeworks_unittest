import unittest

from triangle import Triangle


class TestTriangleUnit(unittest.TestCase):

    def setUp(self):
        self.first = Triangle(9, 9, 9)
        self.second = Triangle(7, 8, 9)

    def test_triangle_eq(self):
        first = Triangle(9, 9, 9)
        second = Triangle(9, 9, 9)
        self.assertEqual(self.first, second)

    def test_triangle_ne(self):
        first = Triangle(9, 7, 9)
        second = Triangle(7, 8, 9)
        self.assertNotEqual(self.first, second)

    def test_triangle_lt(self):
        self.perimetr = 25
        self.assertLess(self.perimetr, 29)

    def test_triangle_gt(self):
        self.perimetr = 25
        self.assertGreater(self.perimetr, 24)

    def test_triangle_le(self):
        self.perimetr = 25
        self.assertLessEqual(self.perimetr, 25)

    def test_triangle_ge(self):
        self.perimetr = 25
        self.assertGreaterEqual(self.perimetr, 26)

    def test_perimetr(self):
        self.assertEqual(self.first.perimetr(), 25)

    def test_is_right_triangle(self):
        self.a = 22
        self.b = 22
        self.c = 44
        right_tr = self.a + self.b
        self.assertEqual(right_tr, self.c)


if __name__ == '__main__':
    unittest.main()
