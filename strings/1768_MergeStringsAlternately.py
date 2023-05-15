class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        out=""
        if len(word1)>len(word2):
            max=len(word1)
            min=len(word2)
            word = word1
        else:
            max=len(word2)
            min = len(word1)
            word = word2
        for i in range(0,min):
            out = out + word1[i]
            out = out + word2[i]
        for i in range(min,max):
            out = out + word[i]
        return out
