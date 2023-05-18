class Solution(object):
    def sortString(self, s):
        counts = [0] * 26  # Count the frequency of each character
        for char in s:
            counts[ord(char) - ord('a')] += 1

        result = []
        while len(result) < len(s):
            # Append smallest characters
            for i in range(26):
                if counts[i] > 0:
                    result.append(chr(i + ord('a')))
                    counts[i] -= 1

            # Append largest characters
            for i in range(25, -1, -1):
                if counts[i] > 0:
                    result.append(chr(i + ord('a')))
                    counts[i] -= 1

        return ''.join(result)

