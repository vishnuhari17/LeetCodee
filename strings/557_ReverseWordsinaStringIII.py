class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list=[]
        for i in s.split():
            list.append(i[::-1])
        return " ".join(list)