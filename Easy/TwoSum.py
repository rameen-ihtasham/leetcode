from typing import List


class Solution:
    def twoSum( nums: List[int], target: int) -> List[int]:
        hashMap = dict()

        for index , num in enumerate(nums):
            required = target - num
            if required in hashMap:
                return [index , hashMap[required]]
            else:
                hashMap[num] = index
        


        
        