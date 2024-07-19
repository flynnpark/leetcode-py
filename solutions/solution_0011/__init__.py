class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            if height[left] > height[right]:
                max_area = max(max_area, height[right] * (right - left))
                right -= 1
            else:
                max_area = max(max_area, height[left] * (right - left))
                left += 1

        return max_area
