class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels=['a', 'e', 'i', 'o','u']
        count = 0
        for i in words[left:right+1]:
            if i[0] in vowels and i[-1] in vowels:
                count += 1
        return count