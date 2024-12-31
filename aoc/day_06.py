import fileinput
from collections import Counter
from collections.abc import Iterable


def main():
    messages = list(map(str.rstrip, fileinput.input()))

    print(part_1(messages))
    print(part_2(messages))


def part_1(messages: Iterable[str]) -> str:
    return ''.join(Counter(col).most_common(1)[0][0]
                   for col in zip(*messages))


def part_2(messages: Iterable[str]) -> str:
    return ''.join(Counter(col).most_common()[-1][0]
                   for col in zip(*messages))


if __name__ == '__main__':
    main()
