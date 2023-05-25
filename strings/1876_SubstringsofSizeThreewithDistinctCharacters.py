class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0,len(s)-2):
            list=[]
            k=i+3
            while i < k:
                if s[i] not in list:
                    list.append(s[i])
                i = i+1
            if len(list) == 3:
                count += 1
        return count