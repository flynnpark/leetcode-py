class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        ranges = []
        start = end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                ranges.append(f'{start}->{end}' if start != end else str(start))
                start = end = nums[i]
        ranges.append(f'{start}->{end}' if start != end else str(start))
        return ranges
