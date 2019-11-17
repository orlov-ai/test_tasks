def count_within_group(x: list, dt: float) -> list:
    """
    Two pointers algorithm. Start two pointer from last point. Decrease i (left point) if within dt.
    Decrease j (right point) if difference of values between points > dt.
    :param x: sorted list of values in subgroup
    :param dt: max difference between point values
    :return: list, number of points with values < dt for each point in a subgroup (x)
    """
    assert list(x) == sorted(x), 'list "x" must be sorted before'
    assert len(x) > 0
    i, j = len(x) - 1, len(x) - 1
    counter = [0] * len(x)
    while True:
        if j < 0:
            break
        elif i < 0:
            j -= 1
            i = j
        elif j == i:
            i -= 1
        elif x[j] - x[i] <= dt:
            counter[j] += 1
            i -= 1
        else:
            j -= 1
            i = j
    return counter


if __name__ == "__main__":
    dt = 0.3
    cases = [([0.206520219143, 0.569711498585, 0.694181201747], [0, 0, 1]),
             ([0.233725001118, 0.593264390713], [0, 0]),
             ([0.760992754734, 0.906011017725, 0.99224586863, ], [0, 1, 2]),
             ([0.823812651856, 0.92776979943], [0, 1]),
             ([0, 1, 2], [0, 0, 0])]
    for input, answer in cases:
        assert count_within_group(input, dt) == answer
