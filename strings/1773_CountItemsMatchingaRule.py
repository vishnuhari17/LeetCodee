class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count = 0
        s = {"type":0,"color":1,"name":2}
        for n in items:
            if n[s.get(ruleKey)]== ruleValue:
                count += 1
        return count