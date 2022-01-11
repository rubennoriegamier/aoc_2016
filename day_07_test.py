from unittest import TestCase, main

from day_07 import is_abba, has_abba, part_1, is_aba, get_abas, aba_to_bab, part_2


class TestDay07(TestCase):
    def test_is_abba(self):
        self.assertTrue(is_abba('abba'))

    def test_is_not_abba(self):
        self.assertFalse(is_abba('aaaa'))

    def test_has_abba(self):
        for sequence in ['abba', 'ioxxoj']:
            with self.subTest(sequence=sequence):
                self.assertTrue(has_abba(sequence))

    def test_does_not_have_abba(self):
        for sequence in ['aaaa', 'zxcvbn']:
            with self.subTest(sequence=sequence):
                self.assertFalse(has_abba(sequence))

    def test_part_1(self):
        self.assertEqual(part_1(['abba[mnop]qrst', 'abcd[bddb]xyyx', 'aaaa[qwer]tyui', 'ioxxoj[asdfgh]zxcvbn']), 2)

    def test_is_aba(self):
        self.assertTrue(is_aba('aba'))

    def test_is_not_aba(self):
        self.assertFalse(is_aba('aaa'))

    def test_get_abas(self):
        self.assertListEqual(list(get_abas('zazbz')), [('z', 'a', 'z'), ('z', 'b', 'z')])

    def test_aba_to_bab(self):
        self.assertEqual(aba_to_bab('aba'), 'bab')

    def test_part_2(self):
        self.assertEqual(part_2(['aba[bab]xyz', 'xyx[xyx]xyx', 'aaa[kek]eke', 'zazbz[bzb]cdb']), 3)


if __name__ == '__main__':
    main()
