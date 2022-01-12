from unittest import TestCase, main

from day_09 import part_1, part_2


class TestDay09(TestCase):
    def test_part_1(self):
        for compressed, uncompressed_length in [('ADVENT', 6),
                                                ('A(1x5)BC', 7),
                                                ('(3x3)XYZ', 9),
                                                ('A(2x2)BCD(2x2)EFG', 11),
                                                ('(6x1)(1x3)A', 6),
                                                ('X(8x2)(3x3)ABCY', 18)]:
            with self.subTest(compressed=compressed):
                self.assertEqual(part_1(compressed), uncompressed_length)

    def test_part_2(self):
        for compressed, uncompressed_length in [('(3x3)XYZ', 9),
                                                ('X(8x2)(3x3)ABCY', 20),
                                                ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241_920),
                                                ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445)]:
            with self.subTest(compressed=compressed):
                self.assertEqual(part_2(compressed), uncompressed_length)


if __name__ == '__main__':
    main()
