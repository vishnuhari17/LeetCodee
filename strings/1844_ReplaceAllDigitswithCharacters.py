class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        out =""
        def shift(c,x):
            i = ord(c)+int(x)
            return chr(i)

        for i in range(1,len(s),2):
            out = out + s[i-1] + shift(s[i-1],s[i])
        if s[-1].isalpha():
            out = out + s[-1]
        return out