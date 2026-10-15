class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in (range(0, len(nums), 2)):

            if i + 1 >= len(nums) or nums[i] != nums[i + 1]:
                return nums[i]