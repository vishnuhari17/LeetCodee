class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start=[]
        for i in range(0,len(paths)):
            start.append(paths[i][0])
        for i in range(0,len(paths)):
            if paths[i][1] not in start:
                return paths[i][1]