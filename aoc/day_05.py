from _md5 import md5
from itertools import count


def main():
    door_id = input()

    print(part_1(door_id))
    print(part_2(door_id))


def part_1(door_id: str) -> str:
    template = f'{door_id}%i'.encode()
    password = []

    for i in count():
        digest = md5(template % i).digest()

        if digest[0] == 0 and digest[1] == 0 and digest[2] < 16:
            password.append(hex(digest[2])[2:])
            if len(password) == 8:
                return ''.join(password)


def part_2(door_id: str) -> str:
    template = f'{door_id}%i'.encode()
    password = ['' for _ in range(8)]

    for i in count():
        digest = md5(template % i).digest()

        if digest[0] == 0 and digest[1] == 0 and digest[2] < 8 and not password[digest[2]]:
            password[digest[2]] = hex(digest[3] >> 4)[2:]

            if all(password):
                return ''.join(password)


if __name__ == '__main__':
    main()
