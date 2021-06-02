class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2 ** 31 - 1 or x <= -(2 ** 31):
            return 0

        temp = str(x)
        if x < 0:
            result = int(f"-{temp[1:][::-1]}")
        else:
            result = int(temp[::-1])

        if result >= 2 ** 31 - 1 or result <= -(2 ** 31):
            return 0
        return result
