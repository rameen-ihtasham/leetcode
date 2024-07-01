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
            
        dictionary = sorted(dictionary.items() , key=lambda x:x[1] , reverse=True)

        for i in range(k):
            result.append(dictionary[i][0])
        
        return result
        
        

Solution.topKFrequent(Solution,[1,2,2,1,2,2,2,5,4] , 2)
