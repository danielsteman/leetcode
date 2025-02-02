class Solution:
    def get_factorial(self, n: int) -> int:
        x = 1
        for i in range(1, n + 1):
            x *= i
        return x

    def get_permutation(self, n: int) -> int:
        return int(self.get_factorial(n) / self.get_factorial(n - 2))

    def climbStairs(self, n: int) -> int:
        """
        fn(1) -> (1)
        fn(2) -> (1,1),(2)
        fn(3) -> (1,1,1),(1,2),(2,1)
        fn(4) -> (1,1,1,1),(1,1,2),(2,1,1),(1,2,1),(2,2)
        fibonacci
        """
        if n == 1:
            return 1

        if n == 2:
            return 2

        a, b = 1, 2
        for _ in range(3, n):
            c = a
            a = b
            b = c + b

            print(f"a: {a}")
            print(f"b: {b}")

        print()
        return a + b


if __name__ == "__main__":
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))
    print(Solution().climbStairs(4))
