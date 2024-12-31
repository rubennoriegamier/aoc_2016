from aoc.day_07 import part_1, part_2


def test_part_1():
    assert part_1(['abba[mnop]qrst',
                   'abcd[bddb]xyyx',
                   'aaaa[qwer]tyui',
                   'ioxxoj[asdfgh]zxcvbn']) == 2


def test_part_2():
    assert part_2(['aba[bab]xyz',
                   'xyx[xyx]xyx',
                   'aaa[kek]eke',
                   'zazbz[bzb]cdb']) == 3
