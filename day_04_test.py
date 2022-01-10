from unittest import TestCase, main

from day_04 import parse_room, part_1


class TestDay04(TestCase):
    def setUp(self):
        self._rooms = list(map(parse_room, ['aaaaa-bbb-z-y-x-123[abxyz]',
                                            'a-b-c-d-e-f-g-h-987[abcde]',
                                            'not-a-real-room-404[oarel]',
                                            'totally-real-room-200[decoy]']))

    def test_part_1(self):
        self.assertEqual(part_1(self._rooms), 1_514)


if __name__ == '__main__':
    main()
