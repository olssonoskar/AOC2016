import file

class Day02:

    def __init__(self, x = 1, y = 1):
        self.x = x
        self.y = y

    def part1(self, filename ="day02/input.txt"):
        content = file.read(filename)
        commands = list(map(str.strip, content.split("\n")))
        return list(map(self.keypad_movement, commands))

    #    1
    #  2 3 4
    #5 6 7 8 9
    #  A B C
    #    D
    # Part 2 uses strange keypad above, we start at '5' so update position before starting
    def part2(self, filename ="day02/input.txt"):
        self.x = -2
        self.y = 0
        content = file.read(filename)
        commands = list(map(str.strip, content.split("\n")))
        result = list(map(self.strange_keypad_movement, commands))
        # Convert to hexadecimal
        return list(map(lambda e: f'{e:X}', result))

    def keypad_movement(self, commands):
        for command in list(commands):
            delta = self.delta(command)
            if self.on_keypad(delta[0], delta[1]):
                self.x += delta[0]
                self.y += delta[1]
        return self.position_to_key()

    def strange_keypad_movement(self, commands):
        for command in list(commands):
            delta = self.delta(command)
            if self.on_strange_keypad(delta[0], delta[1]):
                self.x += delta[0]
                self.y += delta[1]
        return self.strange_position_to_key()

    def delta(self, command):
        x = 0
        y = 0
        match command:
            case "U":
                y = 1
            case "D":
                y = -1
            case "L":
                x = -1
            case "R":
                x = 1
        return x, y

    # Value based on position on a traditional 3x3 keypad
    def position_to_key(self):
        return (7 - self.y * 3) + self.x

    # Value based on position on a leaning square formed keypad
    def strange_position_to_key(self):
        y = 0
        match self.y:
            case -2:
                y = 13
            case -1:
                y = 11
            case 0:
                y = 7
            case 1:
                y = 3
            case 2:
                y = 1
        return y + self.x

    def on_keypad(self, x, y):
        if self.x + x > 2 or self.x + x < 0:
            return False
        if self.y + y > 2 or self.y + y < 0:
            return False
        return True

    def on_strange_keypad(self, x, y):
        if self.y + y > 2 or self.y + y < -2:
            return False
        new_y = self.y + y
        if self.x + x not in self.strange_keypad_x(new_y):
            return False
        return True

    # Valid x positions based on y level
    def strange_keypad_x(self, y):
        strange_keypad_index = [-2, -1, 0, 1, 2]
        return strange_keypad_index[abs(y):len(strange_keypad_index)-abs(y)]