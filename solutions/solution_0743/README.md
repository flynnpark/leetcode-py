## 0743. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)`, where `u<sub>i</sub>` is the source node, `v<sub>i</sub>` is the target node, and `w<sub>i</sub>` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return _the **minimum** time it takes for all the `n` nodes to receive the signal_. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

#### **Example 1:**

![](../../images/0743.jpg)

<pre><code><strong>Input:</strong> times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
<strong>Output:</strong> 2</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> times = [[1,2,1]], n = 2, k = 1
<strong>Output:</strong> 1</code></pre>

#### **Example 3:**

<pre><code><strong>Input:</strong> times = [[1,2,1]], n = 2, k = 2
<strong>Output:</strong> -1</code></pre>

#### **Constraints:**

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= u<sub>i</sub>, v<sub>i</sub> <= n`
- `u<sub>i</sub> != v<sub>i</sub>`
- `0 <= w<sub>i</sub> <= 100`
- All the pairs `(u<sub>i</sub>, v<sub>i</sub>)` are **unique**. (i.e., no multiple edges.)

## 문제 해결

이 문제에서 판별해야 하는 건 2가지이다.

1. 모든 노드가 신호를 받는 데 걸리는 시간
2. 모든 노드에 도달할 수 있는지 여부

먼저 첫 번째 조건인 '모든 노드가 신호를 받는 데 걸리는 시간'이란 가장 오래 걸리는 노드까지 걸리는 시간이라 할 수 있다. 이는 다익스트라 알고리즘을 통해 구할 수 있다.

두 번째 조건인 '모든 노드에 도달할 수 있는지 여부'도 역시 다익스트라 알고리즘을 이용하여 모든 노드의 계산 값이 존재하는지 유무로 판별할 수 있다.

여기서는 파이썬에서 우선순위 큐를 최소 힙으로 구현한 `heapq`를 사용하여 구현하였다.

```python
def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
  graph = collections.defaultdict(list)

  for u, v, w in times:
      graph[u].append((v, w)) # 그래프 구조 생성

  q = [(0, k)] # 시작점에서 각 정점가지의 소요 시간을 담기 위한 큐
  dist = collections.defaultdict(int) # 정점까지의 최단 거리를 담기 위한 딕셔너리

  while q:
      time, node = heapq.heappop(q) # 큐에서 가장 작은 시간을 가진 정점을 꺼냄
      if node not in dist:
          dist[node] = time # node까지의 거리가 기록되어 있지 않다면 기록

          for v, w in graph[node]: # node에서 연결된 정점들을 돌면서 걸리는 시간을 계산하여 큐에 저장
              alt = time + w
              heapq.heappush(q, (alt, v))

  if len(dist) == n: # 모든 노드까지의 거리가 기록되어 있다면 모든 노드가 신호를 받을 수 있는 시간을 반환
      return max(dist.values())

  return -1 # 기록된 노드의 갯수가 전체 노드의 갯수와 다르다면 값을 구할 수 없으므로 -1 반환
```
