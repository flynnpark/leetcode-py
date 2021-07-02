# 0053. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return _its sum_.

#### Example 1:

<pre><code><strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [4,-1,2,1] has the largest sum = 6.</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1</code></pre>

#### Example 3:

<pre><code><strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23</code></pre>

#### Constraints:

- `1 <= nums.length <= 3 * 10<sup>4</sup>`
- `-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>`

## 해결 방법

주어진 숫자의 배열 중 부분합의 크기가 가장 큰 값을 구하는 문제이다. 이걸 어떻게 할까 하다가 결국 그냥 부분합 알고리즘을 검색 했다. 그러니 카데인 알고리즘이라는 게 나왔다. `nums[i]`의 부분합은 `nums[i-1]`의 부분합 + `nums[i]`를 통해서 구할 수 있기 때문에, `nums[i]`의 모든 부분합을 다시 계산하지 않아도 된다는 것이다. 이를 응용하자면, `nums[i]`의 부분합 중 최댓값은 `nums[i-1]`의 부분합 중 최댓값 + `nums[i]` 또는 `nums[i]` 중 큰 값이 되는 것이다. 이를 코드로 구현한다면, `i`는 `i-1`과의 비교를 위해 0이 아닌 1부터 배열의 길이가 되고, `nums[i]`와 `nums[i] + nums[i - 1]`의 최댓값을 `nums[i]`에 반영한 후 최종적으로 만들어진 `nums` 배열의 최댓값을 반환하면 된다.
