class Solution:
    def repeatedCharacter(self, s: str) -> str:
        list = []
        for i in s:
            if i in list:
                return i
            list.append(i)