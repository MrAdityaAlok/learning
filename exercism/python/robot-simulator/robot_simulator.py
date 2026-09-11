NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    def __init__(self, direction: int = NORTH, x_pos: int = 0, y_pos: int = 0) -> None:
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    @property
    def coordinates(self) -> tuple[int, int]:
        return self.x_pos, self.y_pos

    def move(self, instructions: str) -> None:
        for instruction in instructions:
            match instruction:
                case "R":
                    self.direction = (self.direction + 1) % 4
                case "L":
                    self.direction = (self.direction - 1) % 4
                case "A":
                    if self.direction == NORTH:
                        self.y_pos += 1
                    elif self.direction == SOUTH:
                        self.y_pos -= 1
                    elif self.direction == EAST:
                        self.x_pos += 1
                    else:
                        self.x_pos -= 1
