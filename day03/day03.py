import file


def part1(filename="day03/input.txt"):
    content = file.read_lines(filename)
    count = 0
    for line in content:
        if valid_triangle(convert_row(line)):
            count += 1
    return count


def part2(filename="day03/input.txt"):
    content = file.read_lines(filename)
    count = 0
    for i in range(0, len(content), 3):
        count += check_columns([convert_row(content[i]),
                                convert_row(content[i + 1]),
                                convert_row(content[i + 2])])
    return count

# Take 3 rows and form triangles on columns instead of rows
def check_columns(rows):
    count = 0
    for i in range(0, 3):
        if valid_triangle([rows[0][i], rows[1][i], rows[2][i]]):
            count += 1
    return count


def convert_row(row):
    sides = list(map(str.strip, row.split(" ")))
    return list(filter(lambda value: len(value) > 0, sides))

# Valid triangle if all pair of legs are longer than remaining one
def valid_triangle(legs):
    return (is_larger(legs[0], legs[1], legs[2])
            and is_larger(legs[1], legs[2], legs[0])
            and is_larger(legs[2], legs[0], legs[1]))


def is_larger(a, b, c):
    return int(a) + int(b) > int(c)
