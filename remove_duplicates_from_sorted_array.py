class Solution:
    @classmethod
    def removeDuplicates(cls, nums: list[int]) -> int:
        n = len(nums)
        k = 0
        last = nums[n - 1]
        first = nums[0]
        for i in range(1, n - 2):
            if (n - i) < i:
                break
            print(f"{nums[i]} should not be {first}")
            if nums[i] != first:
                k += 1
            print(f"{nums[n-i]} should not be {last}")
            if nums[n - i] != last:
                k += 1
            first = nums[i]
            last = nums[n - i]
        return k


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution.removeDuplicates(nums)
print(solution)
