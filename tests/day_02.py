from pytest import fixture

from aoc.day_02 import part_1, part_2


@fixture
def instructions() -> list[str]:
    return ['ULL',
            'RRDDD',
            'LURDL',
            'UUUUD']


def test_part_1(instructions):
    assert part_1(instructions) == 1985


def test_part_2(instructions):
    assert part_2(instructions) == '5DB3'
