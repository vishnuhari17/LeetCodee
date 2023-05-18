class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        v=('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        l=len(s)//2
        ac=0
        a=s[0:l]
        b=s[l:]
        for i in range(0,l) :
            if a[i] in v:
                ac += 1
            if b[i] in v:
                ac -= 1
        if ac == 0:
            return True
        else:
            return False