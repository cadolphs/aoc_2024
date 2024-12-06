from day06 import Map, has_loop, place_obstacle


def test_can_query_inside_of_map():
    my_map = Map.from_string("..#\n#.#\n#..")

    for x in range(3):
        for y in range(3):
            assert my_map.is_inbounds(x, y)
    assert not my_map.is_inbounds(3, 2)
    assert not my_map.is_inbounds(2, 3)
    assert not my_map.is_inbounds(-1, 0)
    assert not my_map.is_inbounds(0, -1)


def test_can_query_for_obstacle():
    my_map = Map.from_string("..#\n#.#\n#..")

    obstacle_positions = [(2, 0), (0, 1), (2, 1), (0, 2)]
    for x, y in ((i, j) for i in range(3) for j in range(3)):
        if (x, y) in obstacle_positions:
            assert my_map.is_obstacle(x, y)
        else:
            assert not my_map.is_obstacle(x, y)


def test_gets_the_guard_position():
    my_map = Map.from_string(">..\n...\n...")

    assert my_map.guard_position == (0, 0)
    assert my_map.guard_direction == ">"


def test_turning_90_degrees():
    map_string = "^"
    my_map = Map.from_string(map_string)
    my_map.turn_right()
    assert my_map.guard_direction == ">"
    my_map.turn_right()
    assert my_map.guard_direction == "v"
    my_map.turn_right()
    assert my_map.guard_direction == "<"
    my_map.turn_right()
    assert my_map.guard_direction == "^"


def test_detect_obstacle_in_front():
    map_string = ">#"
    my_map = Map.from_string(map_string)
    assert my_map.obstacle_in_front()

    map_string = ">\n#"
    my_map = Map.from_string(map_string)
    assert not my_map.obstacle_in_front()


def test_step_forward():
    my_map = Map.from_string(">.\n..")
    my_map.step_forward()
    assert my_map.guard_position == (1, 0)


def test_execute_step():
    my_map = Map.from_string(">.#\n...")
    my_map.execute_step()
    assert my_map.guard_position == (1, 0)
    assert my_map.guard_direction == ">"
    my_map.execute_step()
    assert my_map.guard_position == (1, 0)
    assert my_map.guard_direction == "v"
    my_map.execute_step()
    assert my_map.guard_position == (1, 1)
    assert my_map.guard_direction == "v"
    my_map.execute_step()
    assert my_map.guard_position == (1, 2)


def test_map_has_loop():
    my_map = Map.from_string(">.#\n...")
    assert not has_loop(my_map)

    my_map = Map.from_string("####\n#>.#\n#..#\n####")
    assert has_loop(my_map)


def test_place_obstacle():
    my_map = Map.from_string("...\n...\n...")
    new_map = place_obstacle(my_map, 1, 1)
    assert str(new_map) == "...\n.#.\n..."
