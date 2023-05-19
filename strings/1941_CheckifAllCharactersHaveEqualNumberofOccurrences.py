class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 0
            dict[i] += 1
        for i in dict.values():
            if i != list(dict.values())[0]:
                return False
        return True
