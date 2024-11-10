from day01.day01 import Day01
from day02.day02 import Day02
from day03 import day03


def part1(day):
    return "----- Day " + str(day) + " = "


part_2 = "*     Pt 2 = "


def main():
    run_days()


def run_days():
    print(part1(1) + str(Day01().part1()))
    print(part_2 + str(Day01().part2()))
    print(part1(2) + str(Day02().part1()))
    print(part_2 + str(Day02().part2()))
    print(part1(3) + str(day03.part1()))
    print(part_2 + str(day03.part2()))


if __name__ == "__main__":
    main()
