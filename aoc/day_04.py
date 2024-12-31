import fileinput
from collections import Counter
from collections.abc import Iterable
from itertools import chain
from operator import itemgetter
from typing import Self


def main():
    rooms = list(map(Room.parse, map(str.rstrip, fileinput.input())))

    print(part_1(rooms))
    print(part_2(rooms))


class Room:
    _name: list[str]
    _sector_id: int
    _checksum: str

    def __init__(self, name: list[str], sector_id: int, checksum: str):
        self._name = name.copy()
        self._sector_id = sector_id
        self._checksum = checksum

    @classmethod
    def parse(cls, raw: str) -> Self:
        name_and_sector_id, checksum = raw.split('[')
        *name, sector_id = name_and_sector_id.split('-')

        return cls(name, int(sector_id), checksum[:-1])

    @property
    def sector_id(self) -> int:
        return self._sector_id

    def is_real(self) -> bool:
        counts = Counter(chain.from_iterable(self._name)).items()
        top_5 = sorted(counts, key=lambda count: (-count[1], count[0]))[:5]

        return set(map(itemgetter(0), top_5)) == set(self._checksum)

    def decrypt_name(self) -> str:
        return ' '.join(''.join(chr((ord(char) - 97 + self._sector_id) % 26 + 97)
                                for char in word)
                        for word in self._name)


def part_1(rooms: Iterable[Room]) -> int:
    return sum(room.sector_id
               for room in rooms
               if room.is_real())


def part_2(rooms: Iterable[Room]) -> int:
    return next(room.sector_id
                for room in rooms
                if room.decrypt_name() == 'northpole object storage')


if __name__ == '__main__':
    main()
