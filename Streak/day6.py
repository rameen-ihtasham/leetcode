class Solution(object):
    def replaceWords(dictionary, sentence):
        word = ""
        words = []
        result = []

        for letter in sentence:
            if letter != " ":
                word = word + letter
            else:
                words.append(word)
                word = ""
        words.append(word)

        dictionary.sort()

        for derivative in words : 
            for root in dictionary:
                if (derivative.startswith(root)):
                    derivative = root        
           
            result.append(derivative)
            
        resultStr = " ".join(result)
        
        
        return resultStr
    

print(Solution.replaceWords(["a","b","c"] , "aadsfasf absbs bbab cadsfafs"))
            


        

