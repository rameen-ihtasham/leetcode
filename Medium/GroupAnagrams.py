class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = dict()
        result = []
        for i in range(len(strs)):
            required = str(sorted(strs[i]))
            if required in dictionary:
                dictionary[required].append(i)
            else:
                dictionary[required] = [i]
        for indexes in dictionary.values():
            answer = []
            for index in indexes:
                answer.append(strs[index])
            result.append(answer)
        return result
