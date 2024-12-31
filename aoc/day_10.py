import fileinput
from bisect import insort
from collections import defaultdict, deque
from collections.abc import Iterable


def main():
    instructions = map(str.split, map(str.rstrip, fileinput.input()))

    print(*part_1_and_2(instructions, [17, 61]), sep='\n')


def part_1_and_2(instructions: Iterable[list[str]], values: list[int]) -> tuple[int, int]:
    instructions = deque(instructions)
    bots = defaultdict(list)
    outputs = []

    while instructions:
        instruction = instructions.popleft()

        if instruction[0] == 'value':
            insort(bots[int(instruction[5])], int(instruction[1]))
        elif len(values_ := bots[int(instruction[1])]) == 2:
            if instruction[5] == 'bot':
                insort(bots[int(instruction[6])], values_[0])
            elif int(instruction[6]) <= 2:
                outputs.append(values_[0])
            if instruction[10] == 'bot':
                insort(bots[int(instruction[11])], values_[1])
            elif int(instruction[11]) <= 2:
                outputs.append(values_[1])
        else:
            instructions.append(instruction)

    return next(bot
                for bot, values_ in bots.items()
                if values_ == sorted(values)), outputs[0] * outputs[1] * outputs[2]


if __name__ == '__main__':
    main()
