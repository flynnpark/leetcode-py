## 0207. [Course Schedule](https://leetcode.com/problems/course-schedule/)

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]` indicates that you **must** take course `b<sub>i</sub>` first if you want to take course `a<sub>i</sub>`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

#### **Example 1:**

<pre><code><strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> numCourses = 2, prerequisites = [[1,0],[0,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.</code></pre>

#### **Constraints:**

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= a<sub>i</sub>, b<sub>i</sub> < numCourses`
- All the pairs prerequisites[i] are **unique**.

## 해결 방법

전체 수업의 갯수인 `numCourses`와 수업 0을 완료하기 위해서는 수업 1을 완료해야 한다는 의미로 `[0, 1]`와 같은 전제조건들의 배열인 `prerequisites`가 주어진다. 주어진 정보를 가지고 모든 수업을 완료할 수 있는지 판별하는 문제이다.

```python
graph = collections.defaultdict(list)

for x, y in prerequisites:
    graph[x].append(y)
```

먼저 전제조건인 `prerequisites`를 그래프로 표현한다.

```python
traced = set()

for x in graph:
  if not dfs(x):
    return False

return True
```

순환 구조를 판별하기 위해 이미 방문했던 노드를 traced에 저장한다. 이미 방문했던 곳을 중복 방문하게 된다면 순환 구조로 간주할 수 있다.

```python
def dfs(x):
  if x in traced:
    return False

  traced.add(x)

  for y in graph[x]:
    if not dfs(y):
      return False

  traced.remove(x)
  return True
```

`dfs` 함수에서는 현재 노드가 이미 방문했던 노드의 집합인 `traced`에 존재한다면 순환 구조로 간주하고 `False`를 반환한다. `False`는 계속 상위로 반환되어 최종 결과도 `False`로 반환된다. 탐색을 계속 재귀로 진행하되 해당 노드를 이용한 모든 탐색이 끝났다면 해당 노드를 `traced`에서 제거해야 한다. 그렇지 않으면 순환이 아닌데 순환이라고 잘못 판단할 수 있기 때문이다.

다만 이렇게만 해결 했을 때 기준으로 leetcode에서는 `Time Limit Exceeded` 에러가 발생했다. 그래서 이를 해결하기 위해 이미 방문했던 노드일 경우 더 이상 진행하지 않는 경우를 추가했다.

```python
visited = set()

def dfs(x):
  if x in traced:
    return False

  if x in visited:
    return True

  traced.add(x)

  for y in graph[x]:
    if not dfs(y):
      return False

  traced.remove(x)
  visited.add(x) # 탐색 종료 후 방문한 노드 저장

  return True
```
