class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict={}
        flag=0
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        j=list(dict.values())
        for i in dict.values():
            if i == j[0]:
                continue
            else:
                flag = 1
                break
        if flag == 0:
            return True
        else:
            return False