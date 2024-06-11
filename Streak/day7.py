class Solution(object):
    def heightChecker(heights):
        currentHeights = heights.copy()
        heights.sort()
        wrongOrder = 0
        for i in range(0 , len(heights)):
            if heights[i] != currentHeights[i]:
                wrongOrder += 1
        return wrongOrder

        
print(Solution.heightChecker([5,1,2,3,4]))