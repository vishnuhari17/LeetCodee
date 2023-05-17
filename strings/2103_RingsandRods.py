class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        dict={}
        count = 0
        for i in range(0,len(rings)-1,2):
            j=dict.get(rings[i+1])
            if j == None:
                dict[rings[i+1]]=[rings[i]]
            else:
                if rings[i] not in j:
                    j.append(rings[i])
                    if len(j)==3:
                        count += 1
                    dict[rings[i + 1]]=j
        return count