from pytest import fixture

from aoc.day_06 import part_1, part_2


@fixture
def messages() -> list[str]:
    return ['eedadn',
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


def test_part_1(messages):
    assert part_1(messages) == 'easter'


def test_part_2(messages):
    assert part_2(messages) == 'advent'
