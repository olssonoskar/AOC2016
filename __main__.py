from day01.day01 import Day01
from day02.day02 import Day02


def main():
    run_days()

def run_days():
    print("Day 1 = " + str(Day01().part1()))
    print("Pt 2 = " + str(Day01().part2()))
    print("Day 2 = " + str(Day02().part1()))
    print("Pt 2 = " + str(Day02().part2()))

if __name__ == "__main__":
    main()