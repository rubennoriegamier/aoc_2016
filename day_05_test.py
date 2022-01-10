from unittest import TestCase, main

from day_05 import part_1, part_2


class TestDay05(TestCase):
    def setUp(self):
        self._door_id = 'abc'

    def test_part_1(self):
        self.assertEqual(part_1(self._door_id), '18f47a30')

    def test_part_2(self):
        self.assertEqual(part_2(self._door_id), '05ace8e3')


if __name__ == '__main__':
    main()
