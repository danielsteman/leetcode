class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        result = x
        for _ in range(n - 1):
            result *= x

        return result

    def myPowRecursive(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        count = 0

        if n > 0:
            x = x * self.myPowRecursive(x, n - 1)
            count += 1

        return x


if __name__ == "__main__":
    print(Solution().myPowRecursive(2, 10))
