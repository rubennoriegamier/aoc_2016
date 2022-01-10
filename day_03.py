import fileinput
from itertools import chain


def main():
    triangles = list(map(parse_triangle, fileinput.input()))

    print(part_1(triangles))
    print(part_2(triangles))


def parse_triangle(raw_triangle):
    return tuple(map(int, raw_triangle.split()))


def part_1(triangles):
    return sum(1 for a, b, c in triangles if a + b > c and a + c > b and c + b > a)


def part_2(triangles):
    sides = chain.from_iterable(zip(*triangles))
    valid = 0

    for _ in triangles:
        a = next(sides)
        b = next(sides)
        c = next(sides)

        if a + b > c and a + c > b and c + b > a:
            valid += 1

    return valid


if __name__ == '__main__':
    main()
