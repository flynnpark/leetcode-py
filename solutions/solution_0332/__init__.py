import collections


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        def dfs(a: str):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        route = []
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        dfs('JFK')

        return route[::-1]
