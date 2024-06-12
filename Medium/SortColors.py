class Solution(object):
    def sortColors(nums):
        buckets = [[],[],[]]
        for num in nums :
            buckets[num].append(num)
        result = []
        for bucket in buckets:
            result = result + bucket
        for i in range(len(result)):
            nums[i] = result[i]

        return nums
    
print(Solution.sortColors([2,0,2,1,1,0]))

        