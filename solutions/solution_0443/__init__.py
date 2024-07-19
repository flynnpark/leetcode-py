class Solution:
    def compress(self, chars: list[str]) -> int:
        temp = []
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                temp.append((chars[i - 1], count))
                count = 1
        temp.append([chars[-1], count])

        i = 0
        for key, value in temp:
            chars[i] = key
            i += 1
            if value > 1:
                for num in str(value):
                    chars[i] = num
                    i += 1
        return i
