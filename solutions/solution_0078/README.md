## 0078. [Subsets](https://leetcode.com/problems/subsets/)

Given an integer array `nums` of **unique** elements, return _all possible subsets (the power set)_.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

#### **Example 1:**

<pre><code><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]</code></pre>

#### **Constraints:**

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are unique.

## 해결 방법

이 문제는 다음과 같이 트리를 구성하고 트리를 DFS하는 방식으로 풀이할 수 있다.

```
[1, 2, 3]
1 - 2 = 3
  - 3
2 - 3
3
```

경로 `path`를 만들면서 인덱스를 1씩 증가하는 형태로 깊이 탐색하고, 별도의 종료 조건 없이 탐색이 끝나면 함수가 종료되게 한다. 부분 집합은 모든 탐색의 경로가 정답이 되므로 탐색할 때마다 매번 결과를 추가하면 된다.
