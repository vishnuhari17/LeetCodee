class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max = 0
        for i in strs:
            if i.isdigit() == True:
                val = 0
                for j in i:
                    val = val * 10 + int(j)
                if val > max:
                    max = val
            else:
                if max < len(i):
                    max = len(i)
        return max
