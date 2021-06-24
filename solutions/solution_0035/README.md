# 0035. [Search Insert Position](https://leetcode.com/problems/search-insert-position/)

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

#### Example 1:

<pre><code><strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1</code></pre>

#### Example 3:

<pre><code><strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4</code></pre>

#### Example 4:

<pre><code><strong>Input:</strong> nums = [1,3,5,6], target = 0
<strong>Output:</strong> 0</code></pre>

#### Example 5:

<pre><code><strong>Input:</strong> nums = [1], target = 0
<strong>Output:</strong> 0</code></pre>

#### Constraints:

- `1 <= nums.length <= 10<sup>4</sup>`
- `-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>`
- `nums` contains **distinct** values sorted in **ascending** order.
- `-10<sup>4</sup> <= target <= 10<sup>4</sup>`

## 문제 해결

입력 값으로 정렬된 숫자의 배열 `nums`, 배열에 넣고 싶은 숫자 `target`을 입력받은 후 `target`이 위치할 포지션을 반환하는 문제이다. 단, 문제에서 시간 복잡도는 `O(log n)`이어야 한다고 제한을 두었다.

문제 자체는 어려운 편은 아닌데, 시간 복잡도가 `O(log n)`이어야 하기 때문에 그냥 배열을 순회하는 걸로는 조건을 충족하지 못한다. 그래서 정렬된 리스트에서 `O(log n)`의 시간 복잡도를 가지는 이진 탐색 알고리즘을 사용하여 구현하였다.
