class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        p=1
        while n>0:
            rem=n%10
            s+=rem
            p*=rem
            n=n//10
        result = p - s
        return result