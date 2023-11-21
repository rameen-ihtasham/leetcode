class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 0:
                return True
        return False
