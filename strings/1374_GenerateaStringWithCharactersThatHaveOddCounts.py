class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        out=""
        if n%2==0:
            for i in range(0,n-1):
                out = out + "a"
            out = out + "b"
        else:
            for i in range(0,n):
                out = out + "a"
        return out