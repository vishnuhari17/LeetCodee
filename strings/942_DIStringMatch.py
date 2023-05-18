class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        perm = []
        min = 0
        max = len(s)
        for i in s:
            if i =="I":
                perm.append(min)
                min += 1
            else:
                perm.append(max)
                max -= 1
        if s[-1] == "I":
            perm.append(min)
        else:
            perm.append(max)
        return perm