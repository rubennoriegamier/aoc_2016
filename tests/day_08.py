from aoc.day_08 import parse_instruction, part_1


def test_part_1():
    assert part_1(map(parse_instruction, ['rect 3x2',
                                          'rotate column x=1 by 1',
                                          'rotate row y=0 by 4',
                                          'rotate column x=1 by 1']), 7, 3) == 6
