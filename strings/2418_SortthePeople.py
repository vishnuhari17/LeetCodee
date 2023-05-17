class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        dict={}
        out=[]
        for i in range(0,len(names)):
            dict[heights[i]]=names[i]
        heights.sort(reverse=True)
        for i in heights:
            out.append(dict.get(i))
        return out