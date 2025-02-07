class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        result = x
        for _ in range(n - 1):
            result *= x

        return result


if __name__ == "__main__":
    print(Solution().myPow(2, 10))
