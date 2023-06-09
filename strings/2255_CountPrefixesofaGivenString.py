class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for i in range(len(s)+1):
            if s[:i] in words:
                count += words.count(s[:i])
        return count

# Another approach

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if word == s[:len(word)]:
                count += 1
        return count