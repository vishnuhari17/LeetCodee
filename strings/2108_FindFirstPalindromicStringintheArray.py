class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            list = []
            for i in word:
                list.append(i)
            list.reverse()
            w = "".join(list)
            if w == word:
                return word
                break
        return ""