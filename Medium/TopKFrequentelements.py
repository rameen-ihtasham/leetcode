from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        dictionary = dict()
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
