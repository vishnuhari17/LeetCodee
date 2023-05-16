class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=0
        open=0
        for i in s:
            if max<open:
                    max=open
            if i == "(":
                open += 1
            if i == ")":
                open -= 1
        return max
