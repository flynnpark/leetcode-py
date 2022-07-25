## 0332. [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

You are given a list of airline `tickets` where `tickets[i] = [from<sub>i</sub>, to<sub>i</sub>]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `"JFK"`, thus, the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

- For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

#### **Example 1:**

<pre><code><strong>Input:</strong> tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
<strong>Output:</strong> ["JFK","MUC","LHR","SFO","SJC"]</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
<strong>Output:</strong> ["JFK","ATL","JFK","SFO","ATL","SFO"]
<strong>Explanation:</strong> Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.</code></pre>

#### **Constraints:**

- `1 <= tickets.length <= 300`
- `tickets[i].length == 2`
- `from<sub>i</sub>.length == 3`
- `to<sub>i</sub>.length == 3`
- `from<sub>i</sub>` and `to<sub>i</sub>` consist of uppercase English letters.
- `from<sub>i</sub> != to<sub>i</sub>`

## 문제 해결

`[from, to]`로 구성된 항공권 목록을 사용하여 JFK에서 출발하는 여행 일정을 구성하는데, 출발지가 동일한 항공권이 여러 개 있을 경우 사전 어휘순으로 방문해야하는 문제이다.

여행 일정을 그래프로 구성한 후 DFS로 풀이한다. 이 때, 출발지가 동일한 경우엔 사전 어휘순으로 방문해야한다는 점이다. 먼저 그래프는 아래와 같이 구현할 수 있다.

```python
graph = collections.defaultdict(list)

for a, b in sorted(tickets)
    graph[a].append(b)
```

이제 그래프에서 `pop()`을 통해 재귀호출하면서 결과에 추가한다. 결과에는 역순으로 담기게 될 것이며, `pop` 함수를 통해 처리했기 때문에 그래프에서는 해당 목적지를 재방문하게 되지는 않는다.

```python
def dfs(a):
  while graph(a):
    dfs(graph[a].pop(0))
  route.append(a)
```

어휘순으로 그래프를 생성했기 때문에, `pop(0)`으로 첫 번째 값을 읽어야 한다.

여기서 `pop(0)`은 O(n)이기 때문에 성능을 개선하기 위해서 그래프에 값을 추가하는 부분과 그래프에서 값을 추출하는 부분을 개선한다.

```python
graph = collections.defaultdict(list)

for a, b in sorted(tickets, reverse=True):
    graph[a].append(b)

...

def dfs(a):
  while graph(a):
    dfs(graph[a].pop())
  route.append(a)
```
