import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = collections.defaultdict(int)
        words = re.sub(r"[^\w]", " ", paragraph).lower().split()
        for word in words:
            if word not in banned:
                counts[word] += 1
        return max(counts, key=counts.get)  # type: ignore
