class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        list =[]
        sum = 0
        for i in sentence:
            if i not in list:
                list.append(i)
                sum += ord(i)
        if sum == 2847:
            return True
        else:
            return False
