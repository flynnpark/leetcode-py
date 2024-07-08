from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        t_map: defaultdict[str, int] = defaultdict(int)
        t_length = len(t)

        for char in t:
            t_map[char] += 1

        left = 0
        result = (0, len(s) + 1)

        for right, char in enumerate(s):
            if t_map[char] > 0:
                t_length -= 1

            t_map[char] -= 1

            if t_length == 0:
                while True:
                    current_left = s[left]
                    if t_map[current_left] == 0:
                        break

                    t_map[current_left] += 1
                    left += 1

                if right - left < result[1] - result[0]:
                    result = (left, right)

                t_map[s[left]] += 1
                t_length += 1
                left += 1

        return s[result[0] : result[1] + 1] if result[1] != float('inf') else ''
