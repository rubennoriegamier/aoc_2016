import fileinput
import re
from collections.abc import Iterable

BRACKETS_RE = re.compile(r'[\[\]]')
ABBA_RE = re.compile(r'(.)(?!\1)(.)\2\1')
ABA_RE = re.compile(r'(.)(?!\1)(?=.\1)')


def main():
    ips = list(map(str.rstrip, fileinput.input()))

    print(part_1(ips))
    print(part_2(ips))


def part_1(ips: Iterable[str]) -> int:
    return sum(any(map(ABBA_RE.search, sequences[::2])) and
               not any(map(ABBA_RE.search, sequences[1::2]))
               for sequences in map(BRACKETS_RE.split, ips))


def part_2(ips: Iterable[str]) -> int:
    return sum(len({sequence[match.start():match.start() + 3]
                    for sequence in sequences[::2]
                    for match in ABA_RE.finditer(sequence)} &
                   {f'{sequence[match.start() + 1]}{sequence[match.start()]}{sequence[match.start() + 1]}'
                    for sequence in sequences[1::2]
                    for match in ABA_RE.finditer(sequence)}) > 0
               for sequences in map(BRACKETS_RE.split, ips))


if __name__ == '__main__':
    main()
