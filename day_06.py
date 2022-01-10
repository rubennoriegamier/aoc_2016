import fileinput
from collections import Counter
from operator import itemgetter, methodcaller


def main():
    message_signal = list(map(str.rstrip, fileinput.input()))

    print(part_1(message_signal))
    print(part_2(message_signal))


def part_1(message_signal):
    # noinspection PyTypeChecker
    return ''.join(map(itemgetter(0),
                       map(itemgetter(0),
                           map(methodcaller('most_common', 1),
                               map(Counter, zip(*message_signal))))))


def part_2(message_signal):
    # noinspection PyTypeChecker
    return ''.join(map(itemgetter(0),
                       map(itemgetter(-1),
                           map(Counter.most_common,
                               map(Counter, zip(*message_signal))))))


if __name__ == '__main__':
    main()
