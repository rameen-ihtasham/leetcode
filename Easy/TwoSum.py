from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = [0, 0]
        dictionary = dict()

        for index, number in enumerate(nums):
            dictionary[number] = index

        for i in range(len(nums)):
            second = target - nums[i]
            if second in dictionary:
                if dictionary[second] == i:
                    continue
                array[0] = i
                array[1] = dictionary[second]
                break

        return array
