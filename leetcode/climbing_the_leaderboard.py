def get_index(arr: list[int], val: int):
    """
    val = 45


    iter 1:

    right 6:
    [100, 100, 50, 40, 40, 20, [10]]

    left 0:
    [[100], 100, 50, 40, 40, 20, 10]

    mid 3:
    [100, 100, 50, [40], 40, 20, 10]


    iter 2:

    right 3:
    [100, 100, 50, [40], 40, 20, 10]

    left 0:
    [[100], 100, 50, 40, 40, 20, 10]

    mid 2:
    [100, 100, [50], 40, 40, 20, 10]


    iter 3:

    right 3:
    [100, 100, 50, [40], 40, 20, 10]

    left 3:
    [100, 100, 50, [40], 40, 20, 10]

    mid 2:
    [100, 100, [50], 40, 40, 20, 10]

    >>> 3
    """

    left = 0
    right = len(arr)
    counter = 0
    while left < right:
        mid = (left + right) // 2

        print()
        print(f"iteration: {counter}")
        print(f"right: {right}")
        print(f"left: {left}")
        print(f"mid: {mid}")
        print()

        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            right = mid
        else:
            left = mid + 1

        counter += 1
    return left


if __name__ == "__main__":
    arr = [100, 100, 50, 40, 40, 20, 10]
    val = 45
    result = get_index(arr, val)
    print(result)


def test_get_index():
    arr = [100, 100, 50, 40, 40, 20, 10]
    val = 45
    expected_index = 3
    actual_index = get_index(arr, val)
    assert expected_index == actual_index
