from aocd import get_data


class Map:
    @classmethod
    def from_string(cls, string):
        return cls(string)

    def __init__(self, map_input: str):
        self.map = map_input.split("\n")
        self.width = len(self.map[0])
        self.height = len(self.map)
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                if cell in "<>^v":
                    self.guard_position = (j, i)
                    self.guard_direction = cell
                    break

    def is_inbounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def is_obstacle(self, x: int, y: int) -> bool:
        if self.is_inbounds(x, y):
            return self.map[y][x] == "#"
        return False

    def turn_right(self) -> None:
        match self.guard_direction:
            case "^":
                self.guard_direction = ">"
            case ">":
                self.guard_direction = "v"
            case "v":
                self.guard_direction = "<"
            case "<":
                self.guard_direction = "^"
            case _:
                raise ValueError(f"Invalid direction: {self.guard_direction}")

    def obstacle_in_front(self) -> bool:
        x, y = self.guard_position
        match self.guard_direction:
            case "^":
                return self.is_obstacle(x, y - 1)
            case ">":
                return self.is_obstacle(x + 1, y)
            case "v":
                return self.is_obstacle(x, y + 1)
            case "<":
                return self.is_obstacle(x - 1, y)
            case _:
                raise ValueError(f"Invalid direction: {self.guard_direction}")

    def step_forward(self) -> None:
        x, y = self.guard_position
        match self.guard_direction:
            case "^":
                self.guard_position = (x, y - 1)
            case ">":
                self.guard_position = (x + 1, y)
            case "v":
                self.guard_position = (x, y + 1)
            case "<":
                self.guard_position = (x - 1, y)
            case _:
                raise ValueError(f"Invalid direction: {self.guard_direction}")

    def execute_step(self) -> None:
        if self.obstacle_in_front():
            self.turn_right()
        else:
            self.step_forward()

    def __str__(self) -> str:
        return "\n".join(self.map)


def has_loop(my_map: Map) -> bool:
    visited = set()
    while (
        my_map.is_inbounds(*my_map.guard_position)
        and (my_map.guard_position, my_map.guard_direction) not in visited
    ):
        visited.add((my_map.guard_position, my_map.guard_direction))
        my_map.execute_step()
    return my_map.is_inbounds(*my_map.guard_position)


def place_obstacle(my_map: Map, x: int, y: int) -> Map:
    new_map = Map.from_string(str(my_map))
    new_map.map[y] = new_map.map[y][:x] + "#" + new_map.map[y][x + 1 :]
    return new_map


if __name__ == "__main__":
    data = get_data(day=6, year=2024)
    my_map = Map.from_string(data)
    guard_start = my_map.guard_position

    visited_positions = set()
    while my_map.is_inbounds(*my_map.guard_position):
        visited_positions.add(my_map.guard_position)
        my_map.execute_step()
    print(len(visited_positions))

    visited_positions.remove(guard_start)
    good_positions = set()
    for position in visited_positions:
        new_map = place_obstacle(my_map, *position)
        if has_loop(new_map):
            good_positions.add(position)

    print(len(good_positions))
