class Solution:
    def isFascinating(self, n: int) -> bool:
        for i in range(1,10):
            l=str(n)+str(n*2)+str(n*3)
            if l.count(str(i))!=1:
                return False
        return True