class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        out = []
        out.append(celsius + 273.15)
        out.append(celsius * 1.80 + 32.00)
        return out