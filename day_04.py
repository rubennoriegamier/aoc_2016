import fileinput
from collections import Counter
from operator import itemgetter


def main():
    rooms = list(map(parse_room, map(str.rstrip, fileinput.input())))

    print(part_1(rooms))
    print(part_2(rooms))


def parse_room(raw_room: str):
    name, sector_id_and_checksum = raw_room.rsplit('-', maxsplit=1)
    first_bracket_idx = sector_id_and_checksum.index('[')

    return name, int(sector_id_and_checksum[:first_bracket_idx]), sector_id_and_checksum[first_bracket_idx + 1:-1]


def part_1(rooms):
    return sum(sector_id for name, sector_id, checksum in rooms
               if ''.join(map(itemgetter(0), sorted(Counter(name.replace('-', '')).most_common(),
                                                    key=lambda pair: (-pair[1], pair[0]))[:len(checksum)])) == checksum)


def part_2(rooms):
    return next(sector_id for name, sector_id, checksum in rooms
                if name.translate({code + 97: chr((code + sector_id) % 26 + 97)
                                   for code in range(26)}) == 'northpole-object-storage')


if __name__ == '__main__':
    main()
