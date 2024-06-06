class Solution(object):
    def commonChars(words):
        alphabets  = "abcdefghijklmnopqrstuvwxyz"
        alphaCount = []

        for letter in alphabets:            
            alphaCount.append(words[0].count(letter))
        
        for count in range(len(alphaCount)):
            for word in words:
                if alphaCount[count] <= 0 or word.count(alphabets[count]) <= 0 :
                    alphaCount[count] = 0
                    break
                else:
                    alphaCount[count] = min(alphaCount[count] , word.count(alphabets[count]))
        
        commonLetters = []
        for letter in range(len(alphabets)):
            if alphaCount[letter] > 0:
                for i in range(alphaCount[letter]):
                    commonLetters.append(alphabets[letter])
        
        return commonLetters
    


print(Solution.commonChars(["bella" , "label" , "roller" ]))


                

    


        




