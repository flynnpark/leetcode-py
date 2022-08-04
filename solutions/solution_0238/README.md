## 0238. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

#### **Example 1:**

<pre><code><strong>Input:</strong> nums = [1, 2, 3, 4]
<strong>Output:</strong> [24, 12, 8, 6]</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> nums = [-1, 1, 0, -3, 3]
<strong>Output:</strong> [0, 0, 9, 0, 0]</code></pre>

#### **Constraints:**

- `2 <= nums.length <= 10<sup>5</sup>`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

## 해결 방법

주어진 배열을 가지고 `output[i]`가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 하는 문제이다. 중요한 제약사항이 하나 있는데, `O(n)`의 시간 복잡도와 나눗셈을 사용하지 못한다는 것이다. 그래서 여기서는 자기 자신을 제외하고 왼쪽의 곱셈 결과와 오른족의 곱셈 결과를 곱하는 방법으로 해결했다.

주어진 배열이 `[1, 2, 3, 4]`라고 가정하고, 왼쪽부터 곱한 결과를 결과에 추가한다.

```python
result = []

temp = 1
for i in range(0, len(nums)):
  result.append(temp) # 왼쪽부터 곱하기 때문에 첫번째 아이템은 바로 1을 추가. 이후엔 계산된 temp를 추가
  temp *= nums[i]
```

`nums[0]`의 왼쪽은 아무 것도 없기 때문에 `result`에 을 넣어주고, 이후 `nums[1]`부터는 `temp`에 `nums[i - 1]`을 곱한 값을 `result`에 넣는다. 이렇게 되면 `result`의 값은 `[1, 1, 2, 6]`이 된다.

다믕으로는 오른쪽부터 곱한 결과를 결과에 반영한다.

```python
temp = 1 # temp를 다시 1로 초기화
for i in range(len(nums) - 1, -1, -1): # 배열의 마지막 인덱스부터 첫 번째 인덱스까지 반복
  result[i] *= temp # 이번엔 오른쪽부터 곱하기 때문에 nums[i] 값을 바로 temp를 곱한 값으로 변경
  temp *= nums[i]
```

결과는 `[24, 12, 8, 6]`이 된다.
