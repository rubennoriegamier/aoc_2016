from unittest import TestCase, main

from day_01 import parse_instruction, part_1, part_2


class TestDay01(TestCase):
    def test_part_1(self):
        for instructions, blocks_away in [(['R2', 'L3'], 5), (['R2', 'R2', 'R2'], 2), (['R5', 'L5', 'R5', 'R3'], 12)]:
            with self.subTest(instructions=instructions):
                self.assertEqual(part_1(map(parse_instruction, instructions)), blocks_away)

    def test_part_2(self):
        self.assertEqual(part_2(map(parse_instruction, ['R8', 'R4', 'R4', 'R8'])), 4)


if __name__ == '__main__':
    main()
