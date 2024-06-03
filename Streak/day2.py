class Solution(object):
    def appendCharacters(self,s, t):
        sPointer = 0
        tPointer = 0 
        wordCount = 0

        for i in range(len(s)):
            if tPointer == len(t):
                break
            if t[tPointer] == s[sPointer]:
                tPointer += 1
                sPointer += 1
            elif t[tPointer] != s[sPointer]:
                sPointer += 1
        
        if tPointer < len(t):
            wordCount = len(t) - tPointer      

        return wordCount



        
def main():
    newstr = Solution.appendCharacters("z" , "abcde")
    print(newstr)


if __name__ == "__main__":
    main()    





        