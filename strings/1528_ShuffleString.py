class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        word=""
        for i in range(len(s)):
            word += s[indices.index(i)]
        return word