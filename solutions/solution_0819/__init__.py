import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        counts = collections.defaultdict(int)
        words = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        for word in words:
            if word not in banned:
                counts[word] += 1
        return max(counts, key=counts.get)  # type: ignore
