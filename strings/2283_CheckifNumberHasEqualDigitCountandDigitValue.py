class Solution:
    def digitCount(self, num: str) -> bool:
        dict = {}
        for i in num:
            if int(i) not in dict:
                dict[int(i)] = 0
            dict[int(i)] += 1
        for i in range(0,len(num)):
            if dict.get(int(i)) == None and int(num[i]) == 0:
                continue
            elif dict.get(int(i)) != int(num[i]):
                return False
        return True