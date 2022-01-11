import fileinput
import re
from itertools import chain

BRACKETS_RE = re.compile(r'[\[\]]')


def main():
    ips = list(map(str.rstrip, fileinput.input()))

    print(part_1(ips))
    print(part_2(ips))


def is_abba(chars):
    return chars[0] != chars[1] and chars[0] == chars[3] and chars[1] == chars[2]


def has_abba(chars):
    return any(map(is_abba, zip(chars, chars[1:], chars[2:], chars[3:])))


def part_1(ips):
    return sum(1 for sequences in map(BRACKETS_RE.split, ips)
               if any(map(has_abba, sequences[::2])) and not any(map(has_abba, sequences[1::2])))


def is_aba(chars):
    return chars[0] == chars[2] and chars[0] != chars[1]


def get_abas(chars):
    return filter(is_aba, zip(chars, chars[1:], chars[2:]))


def aba_to_bab(aba):
    return f'{aba[1]}{aba[0]}{aba[1]}'


def part_2(ips):
    ssl = 0

    for sequences in map(BRACKETS_RE.split, ips):
        babs_re = re.compile('|'.join(map(aba_to_bab, chain.from_iterable(map(get_abas, sequences[::2])))))

        if babs_re.pattern and any(map(babs_re.search, sequences[1::2])):
            ssl += 1

    return ssl


if __name__ == '__main__':
    main()
