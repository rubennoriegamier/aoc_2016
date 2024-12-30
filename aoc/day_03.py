import fileinput
from collections.abc import Iterable
from itertools import batched, chain


def main():
    # noinspection PyTypeChecker
    triangles: list[tuple[int, int, int]] = [tuple(map(int, raw_triangle.split()))
                                             for raw_triangle in fileinput.input()]

    print(part_1(triangles))
    print(part_2(triangles))


def part_1(triangles: Iterable[tuple[int, int, int]]) -> int:
    return sum(a + b > c and a + c > b and b + c > a
               for a, b, c in triangles)


def part_2(triangles: Iterable[tuple[int, int, int]]) -> int:
    # noinspection PyTypeChecker
    return part_1(batched(chain.from_iterable(zip(*triangles)), 3))


if __name__ == '__main__':
    main()
