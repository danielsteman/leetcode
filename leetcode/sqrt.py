import math


class Solution:
    def mySqrt(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        x = n / 2
        tolerance = 0.1
        while True:
            print(x)
            next_x = 0.5 * (x + n / x)
            if abs(next_x - x) < tolerance:
                return math.floor(next_x)
            x = next_x


if __name__ == "__main__":
    print(Solution().mySqrt(9))
