from pytest import fixture

from aoc.day_11 import parse_info, part_1


@fixture
def info() -> tuple[int, ...]:
    return parse_info(['The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
                       'The second floor contains a hydrogen generator.',
                       'The third floor contains a lithium generator.',
                       'The fourth floor contains nothing relevant.'])


def test_part_1(info):
    assert part_1(info) == 11
