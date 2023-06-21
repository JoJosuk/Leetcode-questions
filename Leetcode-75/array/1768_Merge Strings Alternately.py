
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        resultstring=''
        for i in range(min(len(word1),len(word2))):
            resultstring+=word1[i]+word2[i]
        if len(word1)-1>i:
            resultstring+=word1[i+1:]
        if len(word2)-1>i:
            resultstring+=word2[i+1:]
        return resultstring
hey=Solution()
print(hey.mergeAlternately("ab","pqrs"))


