class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for i in text.split():
            found = 0
            for j in brokenLetters:
                if j in i:
                    found = 1
            if found != 1:
                count += 1
        return count
