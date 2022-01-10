from unittest import TestCase, main

from day_03 import part_1, part_2


class TestDay03(TestCase):
    def setUp(self):
        self._triangles = [(101, 301, 501),
                           (102, 302, 502),
                           (103, 303, 503),
                           (201, 401, 601),
                           (202, 402, 602),
                           (203, 403, 603)]

    def test_part_1(self):
        self.assertEqual(part_1(self._triangles), 3)

    def test_part_2(self):
        self.assertEqual(part_2(self._triangles), 6)


if __name__ == '__main__':
    main()
