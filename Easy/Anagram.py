class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap  = dict()
        tMap = dict()

        for i in s:
            if i in sMap:
                sMap[i] +=1
            else:
                sMap[i] = 1
        
        for j in t:
            if j in tMap:
                tMap[j] +=1
            else:
                tMap[j] = 1
        
        return sMap == tMap