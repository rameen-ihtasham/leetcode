class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashMap = dict()
        for num in nums:
            if num in hashMap:
                return True
            else:
                hashMap[num] = 1
            
        return False