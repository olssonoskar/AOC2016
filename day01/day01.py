import file

# Create positions based on the static and diff x,y
def horizontal(y, changes):
    return list(map(lambda e: (e, y), changes))

def vertical(x, changes):
    return list(map(lambda e: (x, e), changes))


class Day01:

    def __init__(self):
        self.rotation = 0
        self.x = 0
        self.y = 0

    def part1(self, filename ="day01/input.txt"):
        content = file.read(filename)
        commands = map(str.strip, content.split(","))
        for command in commands:
            self.turn(command[0])
            self.move(int(command[1:]))
        return abs(self.x) + abs(self.y)

    def part2(self, filename ="day01/input.txt"):
        content = file.read(filename)
        commands = map(str.strip, content.split(","))
        # Keep track of the locations, stop when we return to the same pos the first time
        visited = {(-999,-999)}
        for command in commands:
            self.turn(command[0])
            locations = self.move(int(command[1:]))
            for location in locations:
                if location in visited:
                    return abs(location[0]) + abs(location[1])
                else:
                    visited.add(location)
        return -1

    def turn(self, direction):
        if direction == "R":
            self.rotation = (self.rotation + 90) % 360
        if direction == "L":
            self.rotation = (self.rotation - 90) % 360

    # Move and return the locations we moved through
    def move(self, steps):
        match self.rotation:
            case 0:
                self.y += steps
                return vertical(self.x, list(range(self.y - steps, self.y)))
            case 90:
                self.x += steps
                return horizontal(self.y, list(range(self.x - steps, self.x)))
            # Negative step ranges
            case 180:
                self.y -= steps
                return vertical(self.x, list(range(self.y + steps, self.y, -1)))
            case 270:
                self.x -= steps
                return horizontal(self.y, list(range(self.x + steps, self.x, -1)))

