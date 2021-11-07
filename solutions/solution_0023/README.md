## 0232. [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

_Merge all the linked-lists into one sorted linked-list and return it._

#### **Example 1:**

<pre><code><strong>Input:</strong> lists = [[1,4,5],[1,3,4],[2,6]]
<strong>Output:</strong> [1,1,2,3,4,4,5,6]
<strong>Explanation:</strong> The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> lists = []
<strong>Output:</strong> []</code></pre>

#### **Example 1:**

<pre><code><strong>Input:</strong> lists = [[]]
<strong>Output:</strong> []</code></pre>

#### **Constraints:**

- `k == lists.length`
- `0 <= k <= 10<sup>4</sup?`
- `0 <= lists[i].length <= 500`
- `-10<sup>4</sup> <= lists[i][j] <= 10<sup>4</sup>`
- `lists[i]` is sorted in ascending order.
- The sum of `lists[i].length` won't exceed `10<sup>4</sup>`.

## 해결 방법

이미 정렬 된 리스트 k개를 병합하는 문제이다. 이 때, 병합 된 리스트도 정렬이 된 상태여야 한다. 우선순위 큐를 사용하면 쉽게 풀이할 수 있는 문제로, 여기서는 힙을 사용했다.

힙(heap)은 완전 이진 트리의 일종으로 최댓값 및 회솟값 연산을 빠르게 하기 위해 주로 사용된다. 힙에는 부모 노드의 키 값이 자식 모드의 키 값보다 항상 큰 값을 가지는 '최대 힙'과 반대로 부모 노드의 키 값이 자식 노드의 키 값보다 항상 작은 값을 가지는 '최소 힙'이 있다. 파이썬의 `heapq` 모듈은 최소 힙을 지원하므로, 이를 사용하였다. `lists` 리스트에 있는 각 노드의 헤드를 힙에 삽입한 후, `heappop`을 사용하여 꺼내면 가장 작은 값을 가지는 노드부터 꺼낼 수 있다. 꺼내진 노드를 반환할 노드에 연결해주고, 힙에는 꺼내진 노드의 `next` 노드를 넣는 방식으로 하여 모든 노드의 `next`가 남아있지 않을 때까지 반복하면 원하는 결과를 얻을 수 있다.
