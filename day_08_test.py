from unittest import TestCase, main

from day_08 import parse_instruction, part_1


class TestDay08(TestCase):
    def setUp(self):
        self._instructions = list(map(parse_instruction, ['rect 3x2',
                                                          'rotate column x=1 by 1',
                                                          'rotate row y=0 by 4',
                                                          'rotate column x=1 by 1']))

    def test_part_1(self):
        self.assertEqual(part_1(self._instructions, 7, 3), 6)


if __name__ == '__main__':
    main()
