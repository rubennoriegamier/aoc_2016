from hashlib import md5
from itertools import count


def main():
    door_id = input()

    print(part_1(door_id))
    print(part_2(door_id))


def part_1(door_id):
    template = f'{door_id}%i'.encode()
    password = []

    for idx in count():
        hex_digest = md5(template % idx).hexdigest()

        if hex_digest.startswith('00000'):
            password.append(hex_digest[5])
            if len(password) == 8:
                return ''.join(password)


def part_2(door_id):
    template = f'{door_id}%i'.encode()
    password = [None for _ in range(8)]

    for idx in count():
        hex_digest = md5(template % idx).hexdigest()

        if hex_digest.startswith('00000'):
            position = int(hex_digest[5], 16)

            if position < 8 and password[position] is None:
                # noinspection PyTypeChecker
                password[position] = hex_digest[6]

                if all(password):
                    return ''.join(password)


if __name__ == '__main__':
    main()
