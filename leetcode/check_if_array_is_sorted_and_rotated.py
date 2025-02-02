class Solution:
    def rotate(self, nums: list[int]):
        rotated = [nums[i + 1] for i in range(len(nums) - 1)]
        rotated.append(nums[0])
        return rotated

    def is_sorted(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True

    def brute_force_check(self, nums: list[int]) -> bool:
        """
        An array A rotated by x positions results in an array B
        of the same length such that A[i] == B[(i+x) % A.length]

        [1,2,3]
        [0,1,2]
        [3,1,2]
        [2,0,1]
        """
        for _ in nums:
            rotated = self.rotate(nums)
            print(f"rotated: {rotated}")
            sorted_and_rotated = self.is_sorted(rotated)
            print(f"sorted: {sorted_and_rotated}")
            if sorted_and_rotated:
                return True
            print()
            nums = rotated

        return False

    def check(self, nums: list[int]) -> bool:
        """
        Check number of breaks
        """
        breaks = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                breaks += 1
            if breaks > 1:
                return False
        if breaks == 0:
            return True
        if breaks == 1:
            if nums[-1] <= nums[0]:
                return True
        return False


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    result = Solution().brute_force_check(nums)
    print(result)

    result = Solution().check(nums)
    print(result)
