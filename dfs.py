graph: dict[int, list[int]] = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def recursive_dfs(v: int, discovered: list[int] | None = None) -> list[int]:
    if discovered is None:
        discovered = []
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


def iterative_dfs(start_v: int):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            stack.extend(graph[v])
    return discovered


if __name__ == '__main__':
    print(f'recursive dfs: {recursive_dfs(1)}')
    print(f'iterative dfs: {iterative_dfs(1)}')
