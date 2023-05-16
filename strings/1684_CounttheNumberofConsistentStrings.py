class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        not_match=0
        for word in words:
            for w in word:
                if w not in allowed:
                    not_match+=1
                    break
        ans=len(words)-not_match
        return ans
