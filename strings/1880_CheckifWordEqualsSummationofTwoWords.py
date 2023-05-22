class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        sum1 = 0
        sum2 = 0
        sum = 0
        for i in firstWord:
            sum1 = sum1 * 10 + ord(i) - 97
        for i in secondWord:
            sum2 = sum2 * 10 + ord(i) - 97
        for i in targetWord:
            sum = sum * 10 + ord(i) - 97
        if sum1 + sum2 == sum:
            return True
        return False