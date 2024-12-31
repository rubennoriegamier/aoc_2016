from collections.abc import Iterable

from pytest import fixture

from aoc.day_10 import part_1_and_2


@fixture
def instructions() -> Iterable[list[str]]:
    return map(str.split, ['value 5 goes to bot 2',
                           'bot 2 gives low to bot 1 and high to bot 0',
                           'value 3 goes to bot 1',
                           'bot 1 gives low to output 1 and high to bot 0',
                           'bot 0 gives low to output 2 and high to output 0',
                           'value 2 goes to bot 2'])


def test_part_1(instructions):
    assert part_1_and_2(instructions, [2, 5])[0] == 2


def test_part_2(instructions):
    assert part_1_and_2(instructions, [2, 5])[1] == 30
