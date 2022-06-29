class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(elements: list[int]):
            if len(elements) == 0:
                results.append(prev_elements[:])

            for element in elements:
                next_elements = elements[:]
                next_elements.remove(element)

                prev_elements.append(element)
                dfs(next_elements)
                prev_elements.pop()

        results = []
        prev_elements = []
        dfs(nums)
        return results
