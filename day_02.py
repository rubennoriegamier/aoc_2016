import fileinput

PART_2_KEYPAD = ['  1  ',
                 ' 234 ',
                 '56789',
                 ' ABC ',
                 '  D  ']


def main():
    instructions = list(map(str.rstrip, fileinput.input()))

    print(part_1(instructions))
    print(part_2(instructions))


def part_1(instructions):
    buttons = []
    y = 1
    x = 1

    for button_instructions in instructions:
        for instruction in button_instructions:
            match instruction:
                case 'D':
                    y = min(2, y + 1)
                case 'R':
                    x = min(2, x + 1)
                case 'U':
                    y = max(0, y - 1)
                case 'L':
                    x = max(0, x - 1)

        buttons.append(str(y * 3 + x + 1))

    return int(''.join(buttons))


def part_2(instructions):
    buttons = []
    y = 2
    x = 0

    for button_instructions in instructions:
        for instruction in button_instructions:
            match instruction:
                case 'D':
                    if y < 4 and PART_2_KEYPAD[y + 1][x] != ' ':
                        y += 1
                case 'R':
                    if x < 4 and PART_2_KEYPAD[y][x + 1] != ' ':
                        x += 1
                case 'U':
                    if y > 0 and PART_2_KEYPAD[y - 1][x] != ' ':
                        y -= 1
                case 'L':
                    if x > 0 and PART_2_KEYPAD[y][x - 1] != ' ':
                        x -= 1

        buttons.append(PART_2_KEYPAD[y][x])

    return ''.join(buttons)


if __name__ == '__main__':
    main()
