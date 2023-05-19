class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h = 0
        v = 0
        for i in moves:
            if i == "U":
                v += 1
            elif i == "D":
                v -= 1
            elif i == "R":
                h += 1
            elif i == "L":
                h -= 1
        if v == 0 and h == 0:
            return True
        return False
