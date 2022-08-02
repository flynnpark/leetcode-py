## 0561. [Array Partition](https://leetcode.com/problems/array-partition/)

Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a1, b1), (a2, b2), ..., (a<sub>n</sub>, b<sub>n</sub>)` such that the sum of `min(a<sub>i</sub>, b<sub>i</sub>)` for all `i` is **maximized**. Return _the maximized sum_.

#### **Example 1:**

<pre><code><strong>Input:</strong> nums = [1,4,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> nums = [6,2,6,5,1,2]
<strong>Output:</strong> 9
<strong>Explanation:</strong> The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.</code></pre>

#### **Constraints:**

- `1 <= n <= 10<sup>4</sup>`
- `nums.length == 2 * n`
- `-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>`

## 문제 해결

2n개의 정수를 가진 배열이 주어지고, 이를 n개의 쌍으로 나누어 `min(a, b)` 합의 최댓값을찾는 문제이다. `min(a, b)`을 합산했을 때 최대가 되도록 만든다는 것은 결국 `min(a, b)`의 결과가 되도록 커야한다는 것이고, 이는 주어진 배열을 오름차순으로 정렬하여 쌍을 만들어 값을 도출해내면 된다.

여기서는 단순히 주어진 배열을 오름차순으로 정렬한 후 홀수 번(index가 짝수인 경우)만 추출해서 더했는데, 정렬한 배열의 홀수 번째 값이 각 쌍의 `min`값이기 때문이다.
