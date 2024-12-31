def main():
    compressed = input()

    print(part_1(compressed))
    print(part_2(compressed))


def part_1(compressed: str) -> int:
    decompressed_length = 0
    start = 0

    while True:
        try:
            opening_parenthesis_idx = compressed.index('(', start)
        except ValueError:
            return decompressed_length + len(compressed) - start
        closing_parenthesis_idx = compressed.index(')', opening_parenthesis_idx + 4)
        take, repeat = map(int, compressed[opening_parenthesis_idx + 1:closing_parenthesis_idx].split('x'))
        decompressed_length += opening_parenthesis_idx - start + take * repeat
        start = closing_parenthesis_idx + take + 1


def part_2(compressed: str) -> int:
    def solve(start: int, end: int) -> int:
        decompressed_length = 0

        while True:
            try:
                opening_parenthesis_idx = compressed.index('(', start, end)
            except ValueError:
                return decompressed_length + end - start
            closing_parenthesis_idx = compressed.index(')', opening_parenthesis_idx + 4)
            take, repeat = map(int, compressed[opening_parenthesis_idx + 1:closing_parenthesis_idx].split('x'))
            decompressed_length += opening_parenthesis_idx - start + solve(closing_parenthesis_idx + 1,
                                                                           closing_parenthesis_idx + take + 1) * repeat
            start = closing_parenthesis_idx + take + 1

    return solve(0, len(compressed))


if __name__ == '__main__':
    main()
