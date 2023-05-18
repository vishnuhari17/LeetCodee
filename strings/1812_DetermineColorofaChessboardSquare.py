class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        num=ord(coordinates[0])-96+int(coordinates[1])
        if num%2==0:
            return False
        else:
            return True