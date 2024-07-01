class Solution:
    def groupAnagrams(strs):
        hashMap = dict()
        result = []
        for word in strs:
            sWord= str(sorted(word))            
            if sWord in hashMap:
                hashMap[sWord].append(word)
            else:
                hashMap[sWord] = [word]
        
        for value in hashMap.values():            
            result.append(value)
            
        return result
        
            
        

        
Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])