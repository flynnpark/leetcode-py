import collections
import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        q = [(0, k)]
        dist = collections.defaultdict(int)

        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time

                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(q, (alt, v))

        if len(dist) == n:
            return max(dist.values())

        return -1
