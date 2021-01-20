# 0001. Two Sum

Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.
You may assume that each input would have **_exactly_ one solution**, and you may not use thesameelement twice.
You can return the answer in any order.

#### **Example 1:**

<pre><code><strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Output:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]</code></pre>

#### **Example 3:**

<pre><code><strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]</code></pre>

#### **Constraints:**

- 2 <= nums.length <= 10<sup>3</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
- -10<sup>9</sup> <= target <= 10<sup>9</sup>
- **Only one valid answer exists.**

### 해결방법

2중 for문을 사용하면 쉽게 가능하기는 하지만 시간 복잡도가 O(n<sup>2</sup>)가 되기 때문에 다른 방법을 생각해야 했다.
두 번째로 생각했던 방법은 `target` - `num` 결과의 숫자가 존재하는지 확인하고 해당 숫자의 인덱스를 가져오려고 했는데, 문제의 세 번째 예시를 해결하는 데 어려움이 있었고, 결국 해시 테이블을 사용하여 O(n)으로 문제를 해결할 수 있었다.
