class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        dict={}
        x=97
        out=""
        for i in key:
            if i != " " and i not in dict.keys():
                dict[i]=chr(x)
                x += 1
        for j in message:
            if j != " ":
                out += dict.get(j)
            else:
                out += " "
        return out
