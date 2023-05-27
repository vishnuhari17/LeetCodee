class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = i
            else:
                dict[s[i]] = abs(dict.get(s[i])- i +1)
        l = list(dict.values())
        for i in range(len(l)):
            if l[i] != distance[i]:
                return False
        for i in distance[len(l)+1:]:
            if i != 0:
                return False
        return True