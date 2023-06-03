class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = []
        for i in s:
            if i.isalnum() == True:
                j.append(i.lower())
        if "".join(j[::]) != "".join(j[::-1]):
            return False
        return True