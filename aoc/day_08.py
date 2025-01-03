import fileinput
from collections.abc import Iterable

import numpy as np


def main():
    instructions = list(map(parse_instruction, fileinput.input()))

    print(part_1(instructions, 50, 6))
    print(part_2(instructions, 50, 6))


def parse_instruction(raw_instruction: str) -> tuple[str, int, int]:
    chunks = raw_instruction.split()

    if chunks[0] == 'rect':
        # noinspection PyTypeChecker
        return 'rect', *map(int, chunks[1].split('x'))
    if chunks[1] == 'row' or chunks[1] == 'column':
        return chunks[1][:3], int(chunks[2].split('=')[1]), int(chunks[4])

    raise NotImplementedError()


def part_1(instructions: Iterable[tuple[str, int, int]], width: int, height: int):
    screen = np.zeros((height, width), bool)

    for instruction, a, b in instructions:
        match instruction:
            case 'rect':
                screen[:b, :a] = True
            case 'row':
                screen[a] = np.roll(screen[a], b)
            case 'col':
                screen[:, a] = np.roll(screen[:, a], b)

    return screen.sum()


def part_2(instructions: Iterable[tuple[str, int, int]], width: int, height: int):
    screen = np.zeros((height, width), bool)

    for instruction, a, b in instructions:
        match instruction:
            case 'rect':
                screen[:b, :a] = True
            case 'row':
                screen[a] = np.roll(screen[a], b)
            case 'col':
                screen[:, a] = np.roll(screen[:, a], b)

    return '\n'.join(''.join('#' if on else ' '
                             for on in row)
                     for row in screen)


if __name__ == '__main__':
    main()
