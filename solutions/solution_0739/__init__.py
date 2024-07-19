class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                current = stack.pop()
                result[current] = i - current
            stack.append(i)

        return result
