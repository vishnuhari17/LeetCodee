class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        def issorted(list):
            s = "".join(list)
            list.sort()
            if "".join(list) == s:
                return True
        for i in range(len(strs[0])):
            list=[]
            n = 0
            while n < len(strs):
                list.append(strs[n][i])
                n += 1
            if issorted(list) != True:
                count += 1
        return count