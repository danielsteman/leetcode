def get_index(arr: list[int], val: int):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        print(f"mid: {mid}")
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            right = mid
        elif arr[mid] < val:
            left = mid
        else:
            print("wtf")
            return -1

        print(f"right: {right}")
        print(f"left: {left}")
    return left


if __name__ == "__main__":
    arr = [100, 100, 50, 40, 40, 20, 10]
    val = 45
    get_index(arr, val)


def test_get_index():
    arr = [100, 100, 50, 40, 40, 20, 10]
    val = 45
    expected_index = 3
    actual_index = get_index(arr, val)
    assert expected_index == actual_index
