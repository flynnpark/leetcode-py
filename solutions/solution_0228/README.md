# 0228. [Number of Islands](https://leetcode.com/problems/number-of-islands/)

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return _the number of islands_.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

#### Example 1:

<pre><code><strong>Input:</strong> nums = [0,1,2,4,5,7]
<strong>Output:</strong> ["0->2","4->5","7"]
<strong>Explanation:</strong>The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> nums = [0,2,3,4,6,8,9]
<strong>Output:</strong> ["0","2->4","6","8->9"]
<strong>Explanation:</strong> The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"</code></pre>

#### Constraints:

- `0 <= nums.length <= 20`
- `-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1`
- All the values of `nums` are **unique**.
- `nums` is sorted in ascending order.
