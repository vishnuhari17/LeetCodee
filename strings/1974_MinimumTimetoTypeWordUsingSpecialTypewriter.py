class Solution:
    def minTimeToType(self, word: str) -> int:
        pointer = 'a'
        time = 0
        for character in word:
            distance_clockwise = abs(ord(character) - ord(pointer))
            distance_counterclockwise = 26 - distance_clockwise
            distance = min(distance_clockwise, distance_counterclockwise)
            time += distance + 1
            pointer = character
        return time
