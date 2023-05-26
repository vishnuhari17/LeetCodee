class Solution:
    def checkString(self, s: str) -> bool:
        count = 0
        flag = 0
        for i in s:
            if i == 'a' and flag == 0:
                count += 1
            elif i == 'b':
                count += 1
                flag = 1
            else:
                return False
            if count == 0:
                flag = 0
        return True
