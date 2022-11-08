def horizontal_attack(first_position: tuple[int, int], second_position: tuple[int, int]):
    """
    Verifies if first_position's queen can attack the second_position's queen by comparing
    it's line coordinate (first tuple coordinate).
    """

    if first_position[0] == second_position[0]:
        return True

    return False

def diagonal_attack(first_position: tuple[int, int], second_position: tuple[int, int]):
    """
    Verifies if first_position's queen can attack the second_position's queen by comparing
    it's diagonal coordinates. The absolute value of the coordinates difference must be the
    same.
    """

    if abs(first_position[0] - second_position[0]) == abs(first_position[1] - second_position[1]):
        return True

    return False