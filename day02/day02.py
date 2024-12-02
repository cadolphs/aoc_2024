import aocd

data = aocd.get_data(day=2)


def sign(x: int) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def is_safe(report: list[int]) -> bool:
    # Weed out edge cases
    if len(report) < 2:
        return True

    # Check if we're on the all-ascending or all-descending train
    initial_diff = sign(report[1] - report[0])
    if initial_diff == 0:
        return False

    return is_within_tolerance_and_directional(report, initial_diff)


def is_within_tolerance_and_directional(items: list[int], initial_diff: int) -> bool:
    for current_level, previous_level in zip(items[1:], items):
        x = current_level - previous_level
        if sign(x) != initial_diff or abs(x) > 3:
            return False

    return True


answer = sum(1 for line in data.splitlines() if is_safe([int(x) for x in line.split()]))
print(answer)


def is_safe_with_one_offender(report: list[int]) -> bool:
    # Weed out edge cases
    if len(report) < 2:
        return True

    # Just try out all possible deletions
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1 :]):
            return True

    return False


def is_safe_with_one_offender_sophisticated(report: list[int]) -> bool:
    # Don't bother with short list
    if len(report) < 2:
        return True

    # Grab the first three elements
    x0, x1, x2 = report[:3]

    # Check first _just_ for sign
    s0 = sign(x1 - x0)
    s1 = sign(x2 - x1)

    if s0 == 0:
        return is_safe(report[1:])
    elif s1 == 0:
        return is_safe(report[:2] + report[3:])
    elif s0 != s1:
        # In this case we try removing either element
        return (
            is_safe(report[1:])
            or is_safe(report[:1] + report[2:])
            or is_safe(report[:2] + report[3:])
        )

    # Now we know that the first two elements are in the same direction! Next it's about the magnitudes.
    if abs(x1 - x0) > 3:
        # Only one option here: Remove the first element. Other deletion just makes everything bigger
        return is_safe(report[1:])

    if abs(x2 - x1) > 3:
        # Here we must remove the third element, because removing the second element would make the difference between the first and the third element bigger
        return is_safe(report[:2] + report[3:])

    for i in range(1, len(report) - 3):
        x0, x1, x2 = report[i : i + 3]
        # Check the sign
        if sign(x2 - x1) != s1:
            rest_of_list = report[i + 3 :] if i + 3 < len(report) else []
            if sign(x2 - x0) == s1:
                if is_safe([x0, x2] + rest_of_list):
                    return True
            return is_safe([x0, x1] + rest_of_list)
        # Check the magnitude
        if abs(x2 - x1) > 3:
            rest_of_list = report[i + 3 :] if i + 3 < len(report) else []
            # Delete the third element
            return is_safe([x0, x1] + rest_of_list)
    return True


answer = sum(
    1
    for line in data.splitlines()
    if is_safe_with_one_offender_sophisticated([int(x) for x in line.split()])
)
print(answer)

safe_lines_brute_force = {
    line
    for line in data.splitlines()
    if is_safe_with_one_offender([int(x) for x in line.split()])
}

safe_lines_sophisticated = {
    line
    for line in data.splitlines()
    if is_safe_with_one_offender_sophisticated([int(x) for x in line.split()])
}

# find the difference
print(safe_lines_brute_force - safe_lines_sophisticated)

print(is_safe_with_one_offender_sophisticated([12, 10, 7, 8, 4]))
