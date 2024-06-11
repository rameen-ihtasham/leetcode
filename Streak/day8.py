class Solution(object):
    def relativeSortArray( arr1, arr2):       
        sortedByTwo = []
        notPres = []
        for arranged in arr2:
            for number in arr1:
                if arranged == number:
                    sortedByTwo.append(number)
                
        for num in arr1:
            if num not in sortedByTwo:
                notPres.append(num)
        
        notPres.sort()
        return sortedByTwo+notPres

print(Solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))        




