class Solution:
    def removeDuplicates(self, nums: list[int]):
        if not nums:
            return 0

        j = 0

        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                print(f"{nums[i]} and {nums[i+1]}")
                nums[j] = nums[i]
                j += 1

        return j


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
unique_length = Solution().removeDuplicates(nums)
print(nums[:unique_length])
