class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        num = 0
        for i in operations:
            if "+" in i:
                num += 1
            else:
                num -= 1
        return num
