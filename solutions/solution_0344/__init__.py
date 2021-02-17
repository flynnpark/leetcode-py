from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s  # 테스트 코드를 위해 return을 넣었음

    def reverseString2(self, s: List[str]) -> None:
        s.reverse()
        return s  # 테스트 코드를 위해 return을 넣었음
