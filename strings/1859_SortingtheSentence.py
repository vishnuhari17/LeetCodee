class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        num=1
        out=""
        words=s.split()
        while num!=len(words)+1:
            for i in words:
                if str(num) in i:
                    for letter in i:
                        if letter.isalpha():
                            out = out + letter
                    num += 1
                    if num <= len(words):
                        out= out + " "
        return out

