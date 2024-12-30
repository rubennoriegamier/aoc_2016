from pytest import fixture

from aoc.day_03 import part_1, part_2


@fixture
def triangles() -> list[tuple[int, int, int]]:
    return [(101, 301, 501),
            (102, 302, 502),
            (103, 303, 503),
            (201, 401, 601),
            (202, 402, 602),
            (203, 403, 603)]


def test_part_1(triangles):
    assert part_1(triangles) == 3


def test_part_2(triangles):
    assert part_2(triangles) == 6
