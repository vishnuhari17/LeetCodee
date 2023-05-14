class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        l = 0
        count = 0
        for i in s:
            if i=="R":
                r += 1
            else:
                l += 1
            if r == l:
                count += 1
                r = 0
                l = 0
        return count