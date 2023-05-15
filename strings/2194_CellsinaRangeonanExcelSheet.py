class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        out=[]
        j=s.split(":")
        c1=ord(j[0][0])
        r1=int(j[0][1])
        c2=ord(j[1][0])
        r2=int(j[1][1])
        for i in range(c1,c2+1):
            for j in range(r1,r2+1):
                cell=chr(i)+str(j)
                out.append(cell)
        return out
