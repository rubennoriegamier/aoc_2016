from collections import deque
from collections.abc import Iterable


def main():
    instructions = input().split(', ')

    print(part_1(instructions))
    print(part_2(instructions))


def part_1(instructions: Iterable[str]) -> int:
    directions = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
    y = 0
    x = 0

    for instruction in instructions:
        directions.rotate(1 if instruction[0] == 'L' else -1)
        y += int(instruction[1:]) * directions[0][0]
        x += int(instruction[1:]) * directions[0][1]

    return abs(y) + abs(x)


def part_2(instructions: Iterable[str]) -> int:
    directions = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
    y = 0
    x = 0
    path = {(y, x)}

    for instruction in instructions:
        directions.rotate(1 if instruction[0] == 'L' else -1)
        if directions[0][0]:
            for _ in range(int(instruction[1:])):
                y += directions[0][0]
                if (y, x) in path:
                    return abs(y) + abs(x)
                path.add((y, x))
        else:
            for _ in range(int(instruction[1:])):
                x += directions[0][1]
                if (y, x) in path:
                    return abs(y) + abs(x)
                path.add((y, x))

    return -1


if __name__ == '__main__':
    main()
