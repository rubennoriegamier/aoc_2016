import fileinput
import re
from collections.abc import Iterable, Sequence
from functools import partial
from itertools import chain
from operator import eq


def main():
    info = parse_info(fileinput.input())

    print(part_1(info))
    print(part_2(info))


def parse_info(info: Iterable[str]) -> tuple[int, ...]:
    generators = {}
    microchips = {}

    for floor, floor_info in enumerate(info):
        for element, kind in map(str.split, re.findall(r'\w+[ -](?:generator|compatible microchip)', floor_info)):
            if kind == 'generator':
                generators[element] = floor
            else:
                microchips[element.split('-')[0]] = floor

    return tuple(chain([0], chain.from_iterable((floor, generators[element])
                                                for element, floor in sorted(microchips.items()))))


def is_valid(info: Sequence[int]) -> bool:
    generators = set(info[2::2])

    return all(info[i] == info[i + 1] or
               info[i] not in generators
               for i in range(1, len(info), 2))


def part_1(info: tuple[int, ...]) -> int | None:
    bfs = {info}
    bfs_ = set()
    prev = set()
    steps = 0

    eq_3 = partial(eq, 3)

    while bfs:
        if (info := bfs.pop()) not in prev:
            prev.add(info)

            if is_valid(info):
                if all(map(eq_3, info)):
                    return steps

                elevator = info[0]
                info = list(info)
                offsets = []
                if elevator < 3:
                    offsets.append(1)
                if elevator > 0:
                    offsets.append(-1)

                for offset in offsets:
                    info[0] += offset
                    for i in range(1, len(info)):
                        if info[i] == elevator:
                            info[i] += offset
                            bfs_.add(tuple(info))
                            for j in range(i + 1, len(info)):
                                if info[j] == elevator:
                                    info[j] += offset
                                    bfs_.add(tuple(info))
                                    info[j] -= offset
                            info[i] -= offset
                    info[0] -= offset

        if not bfs:
            bfs = bfs_
            bfs_ = set()
            steps += 1


def part_2(info: tuple[int, ...]) -> int | None:
    return part_1(info + (0, 0, 0, 0))


if __name__ == '__main__':
    main()
