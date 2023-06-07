class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        memory=[]
        out = ""
        o=0
        for i in s:
            if i == "(":
                o += 1
            else:
                o -= 1
            memory.append(i)
            if o == 0:
                out = out + "".join(memory[1:len(memory)-1])
                memory = []
        return out



