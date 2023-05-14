class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max=0
        for i in sentences:
            j=len(i.split())
            if max < j:
                max=j
        return max