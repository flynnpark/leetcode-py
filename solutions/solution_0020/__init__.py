class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"]": "[", "}": "{", ")": "("}
        stack = []

        for char in s:
            if char in pair.values():
                stack.append(char)
            elif len(stack) == 0 or stack.pop() != pair[char]:
                return False
        return not stack
