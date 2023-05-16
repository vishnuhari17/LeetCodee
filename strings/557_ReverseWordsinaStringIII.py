class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        out = ""
        list=[]
        count = 0
        for i in s.split():
            count += 1
            for j in i:
                list.append(j)
            out = out + "".join(list[::-1])
            list= []
            if count != len(s.split()):
                out = out + " "
        return out