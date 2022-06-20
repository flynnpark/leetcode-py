import collections
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        top_k = []
        for _ in range(k):
            top_k.append(heapq.heappop(freqs_heap)[1])
        return top_k
