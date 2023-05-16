class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        out= ""
        flag=0
        for i in s:
            if i =="|":
                if flag==0:
                        flag = 1
                else:
                    flag = 0
            if flag!=1:
                out = out + i
        return out.count("*")