class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n=0
        out = ""
        words=s.split()
        while n < k:
            out = out + words[n]
            n += 1
            if n <k:
                out = out + " "
        return out