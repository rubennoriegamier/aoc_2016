from pytest import mark

from aoc.day_01 import part_1, part_2


@mark.parametrize('instructions, distance',
                  [('R2, L3', 5),
                   ('R2, R2, R2', 2),
                   ('R5, L5, R5, R3', 12)])
def test_part_1(instructions: str, distance: int):
    assert part_1(instructions.split(', ')) == distance


def test_part_2():
    assert part_2('R8, R4, R4, R8'.split(', ')) == 4
