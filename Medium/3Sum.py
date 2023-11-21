ystem.Collections.Linq


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            j = 0
            while j < len(nums):
                segment = []
                segment.append(nums[i])
                if nums[i] != nums[j] and j != i:
                    segment.append(nums[j])
                j += 1
                if len(segment) == 3:
                    sum = 0
                    for i in segment:
                        sum += i
                    if sum == 0:
                        result.append(segment)
                    else:
                        segment.pop()
        return result
