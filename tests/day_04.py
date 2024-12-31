from pytest import mark

from aoc.day_04 import Room, part_1


@mark.parametrize('room, is_real', [('aaaaa-bbb-z-y-x-123[abxyz]', True),
                                    ('a-b-c-d-e-f-g-h-987[abcde]', True),
                                    ('not-a-real-room-404[oarel]', True),
                                    ('totally-real-room-200[decoy]', False)])
def test_part_1(room: str, is_real: bool):
    room = Room.parse(room)

    assert part_1([room]) == (room.sector_id if is_real else 0)
