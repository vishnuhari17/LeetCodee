class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        out = ""
        list=[]
        s=word.find(ch)
        for i in word[0:s+1]:
            list.append(i)
        list.reverse()
        out = out + "".join(list)
        out = out +word[s+1:]
        return out