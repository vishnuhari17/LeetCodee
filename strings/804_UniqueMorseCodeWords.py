class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
        "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
        ".--","-..-","-.--","--.."]
        count = []
        for i in words:
            out=""
            for j in i:
                out = out + morse[ord(j)-97]
            if out not in count:
                count.append(out)
        return len(count)