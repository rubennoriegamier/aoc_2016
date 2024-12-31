from aoc.day_05 import part_1, part_2

DOOR_ID = 'abc'


def test_part_1():
    assert part_1(DOOR_ID) == '18f47a30'


def test_part_2():
    assert part_2(DOOR_ID) == '05ace8e3'
