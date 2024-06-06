class Solution(object):
    def longestPalindrome(s):
        if s == "":
            return 0
        
        s = sorted(s)
        pointerOne = 0
        pointerTwo = 1
        seq = 0
        while pointerTwo < len(s):

            if s[pointerOne] == s[pointerTwo]:
                seq += 2
                pointerOne += 2
                pointerTwo += 2
            else:
                pointerOne += 1 
                pointerTwo += 1

        if seq < len(s):
            seq += 1

        return seq
            

        
        


def main():
    newstr = Solution.longestPalindrome("a")
    print(newstr)


if __name__ == "__main__":
    main()    

        