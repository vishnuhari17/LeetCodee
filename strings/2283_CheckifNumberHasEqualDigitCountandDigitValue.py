class Solution:
    def digitCount(self, num: str) -> bool:
        counts = [0] * 10
        for digit in num:
            counts[int(digit)] += 1
        for i in range(len(num)):
            if counts[i] != int(num[i]):
                return False
        return True