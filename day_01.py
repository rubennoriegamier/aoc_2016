def main():
    instructions = list(map(parse_instruction, input().split(', ')))

    print(part_1(instructions))
    print(part_2(instructions))


def parse_instruction(raw_instruction):
    return raw_instruction[0], int(raw_instruction[1:])


def part_1(instructions):
    angle = 0
    y = 0
    x = 0

    for turn, steps in instructions:
        angle = (angle + (90 if turn == 'R' else -90)) % 360

        match angle:
            case 0:
                y += steps
            case 90:
                x += steps
            case 180:
                y -= steps
            case _:
                x -= steps

    return abs(y) + abs(x)


def part_2(instructions):
    angle = 0
    y = 0
    x = 0
    visited = {(y, x)}

    for turn, steps in instructions:
        angle = (angle + (90 if turn == 'R' else -90)) % 360

        match angle:
            case 0:
                for _ in range(steps):
                    y += 1
                    if (y, x) in visited:
                        return abs(y) + abs(x)
                    visited.add((y, x))
            case 90:
                for _ in range(steps):
                    x += 1
                    if (y, x) in visited:
                        return abs(y) + abs(x)
                    visited.add((y, x))
            case 180:
                for _ in range(steps):
                    y -= 1
                    if (y, x) in visited:
                        return abs(y) + abs(x)
                    visited.add((y, x))
            case _:
                for _ in range(steps):
                    x -= 1
                    if (y, x) in visited:
                        return abs(y) + abs(x)
                    visited.add((y, x))


if __name__ == '__main__':
    main()
