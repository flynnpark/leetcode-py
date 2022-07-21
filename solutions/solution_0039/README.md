## 0039. [Combination Sum](https://leetcode.com/problems/combination-sum/)

Given an array of **distinct** integers `candidates` and a target integer `target`, return _a list of all **unique combinations** of_ `candidates` _where the chosen numbers sum to_ `target`. You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number** of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is **guaranteed** that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

#### **Example 1:**

<pre><code><strong>Input:</strong> candidates = [2,3,6,7], target = 7
<strong>Output:</strong> [[2,2,3],[7]]
<strong>Explanation:</strong>
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> candidates = [2,3,5], target = 8
<strong>Output:</strong> [[2,2,2,2],[2,3,3],[3,5]]</code></pre>

#### **Example 3:**

<pre><code><strong>Input:</strong> candidates = [2], target = 1
<strong>Output:</strong> []</code></pre>

#### **Constraints:**

- `1 <= candidates.length <= 30`
- `1 <= candidates[i] <= 200`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 500`

## 해결 방법

주어진 숫자의 배열인 `candidates`의 원소들을 가지고 원하는 수(`target`)을 만들어낼 수 있는 모든 조합을 만들어내는 문제이다. 그래프를 만들어 탐색하며 각각의 값들을 더하다가 합이 `target`와 같아지면 그 때까지의 값들을 결과에 저장하면 된다.

1. DFS를 사용할 것이고, 인자로 원하는 결과값인 `rest_target`, 현재 숫자의 위치인 `index`, 그리고 지금까지의 경로인 `path`를 인자로 받는다.
2. `rest_target`이 0이면 결과에 현재까지의 경로를 저장한다.
3. `rest_target`이 0보다 작으면 `target`을 만들어낼 수 없다는 뜻이므로 백트래킹 한다.
4. 2, 3에 해당하지 않는 경우 반복문을 돌면서 재귀탐색 한다.
5. `index`와 `len(candidates)` 사이의 범위 `i`에 대해서
6. `rest_target`에서 `candidates[i]`를 뺀 값을 다음 `rest_target`으로, 다음 `index`로 `i`로, 다음 `path`에 `candidates[i]`를 추가한 경로를 저장한다.
7. 주어진 `candidates`의 첫 번째 숫자부터 확인해야 하므로 `dfs(target, 0, [])`를 호출한다.
8. 만들어진 `result`를 반환한다.
