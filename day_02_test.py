from unittest import TestCase, main

from day_02 import part_1, part_2


class TestDay02(TestCase):
    def setUp(self):
        self._instructions = ['ULL',
                              'RRDDD',
                              'LURDL',
                              'UUUUD']

    def test_part_1(self):
        self.assertEqual(part_1(self._instructions), 1_985)

    def test_part_2(self):
        self.assertEqual(part_2(self._instructions), '5DB3')


if __name__ == '__main__':
    main()
