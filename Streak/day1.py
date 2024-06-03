class Solution(object):
    def reverseString( self ,s):
        p1 = 0
        p2 = len(s) - 1
        while(p1 < p2):
           varOne = s[p1]
           varTwo = s[p2]
           s[p1] = varTwo
           s[p2] = varOne
           p1 += 1
           p2 -= 1   
        return s
              

        
def main():
    newstr = Solution.reverseString(['R' , 'a' , 'm'])
    print(newstr)


if __name__ == "__main__":
    main()    

    

       
