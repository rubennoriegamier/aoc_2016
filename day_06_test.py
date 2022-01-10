from unittest import TestCase, main

from day_06 import part_1, part_2


class TestDay06(TestCase):
    def setUp(self):
        self._message_signal = ['eedadn',
                                'drvtee',
                                'eandsr',
                                'raavrd',
                                'atevrs',
                                'tsrnev',
                                'sdttsa',
                                'rasrtv',
                                'nssdts',
                                'ntnada',
                                'svetve',
                                'tesnvt',
                                'vntsnd',
                                'vrdear',
                                'dvrsen',
                                'enarar']

    def test_part_1(self):
        self.assertEqual(part_1(self._message_signal), 'easter')

    def test_part_2(self):
        self.assertEqual(part_2(self._message_signal), 'advent')


if __name__ == '__main__':
    main()
