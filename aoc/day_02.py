import fileinput


def main():
    instructions = list(map(str.rstrip, fileinput.input()))

    print(part_1(instructions))
    print(part_2(instructions))


def part_1(instructions: list[str]) -> int:
    keypad = ['123',
              '456',
              '789']
    y = 1
    x = 1
    code = []

    for instructions_ in instructions:
        for instruction in instructions_:
            match instruction:
                case 'U':
                    y = max(y - 1, 0)
                case 'D':
                    y = min(y + 1, 2)
                case 'L':
                    x = max(x - 1, 0)
                case 'R':
                    x = min(x + 1, 2)
        code.append(keypad[y][x])

    return int(''.join(code))


def part_2(instructions: list[str]) -> str:
    keypad = ['  1  ',
              ' 234 ',
              '56789',
              ' ABC ',
              '  D  ']
    y = 2
    x = 0
    code = []

    for instructions_ in instructions:
        for instruction in instructions_:
            match instruction:
                case 'U':
                    if y > 0 and keypad[y - 1][x] != ' ':
                        y -= 1
                case 'D':
                    if y < 4 and keypad[y + 1][x] != ' ':
                        y += 1
                case 'L':
                    if x > 0 and keypad[y][x - 1] != ' ':
                        x -= 1
                case 'R':
                    if x < 4 and keypad[y][x + 1] != ' ':
                        x += 1
        code.append(keypad[y][x])

    return ''.join(code)


if __name__ == '__main__':
    main()
