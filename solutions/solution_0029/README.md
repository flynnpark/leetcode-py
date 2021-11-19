## 0029. [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

Given two integers `dividend` and `divisor`, divide two integers **without** using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, `8.345` would be truncated to `8`, and `-2.7335` would be truncated to `-2`.

Return _the **quotient** after dividing_ `dividend` by `divisor`.

**Note:** Assume we are dealing with an environment that could only store integers within the **32-bit** signed integer range: `[−2<sup>31</sup>, 2<sup>31</sup> − 1]`. For this problem, if the quotient is **strictly greater than** `2<sup>31</sup> - 1`, then return `2<sup>31</sup> - 1`, and if the quotient is **strictly less** than `-2<sup>31</sup>`, then return `-2<sup>31</sup>`.

#### **Example 1:**

<pre><code><strong>Input:</strong> dividend = 10, divisor = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> 10/3 = 3.33333.. which is truncated to 3.</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> dividend = 7, divisor = -3
<strong>Output:</strong> -2
<strong>Explanation:</strong> 7/-3 = -2.33333.. which is truncated to -2.</code></pre>

#### **Example 3:**

<pre><code><strong>Input:</strong> dividend = 0, divisor = 1
<strong>Output:</strong> 0</code></pre>

#### **Example 4:**

<pre><code><strong>Input:</strong> dividend = 1, divisor = 1
<strong>Output:</strong> 1</code></pre>

#### **Constraints:**

- `-2<sup>31</sup> <= dividend, divisor <= 2<sup>31</sup> - 1`
- `divisor != 0`

## 해결 방법

피제수 `dividend`와 제수 `divisor`가 주어지고 피제수를 제수로 나눈 몫을 구하는 문제이다. 이 때, 곱셈이나 나눗셈, 나머지 연산자를 사용하지 못하는 제한 사항이 있었다.

우선 음수에서 양수를 나누거나, 양수에서 음수를 나누는 경우엔 몫이 음수여야 하고, 이 외의 경우엔 양수여야 하기 때문에, 이를 판별하기 위한 `is_positive`를 먼저 구한다. 그리고 양수로 만든 `dividend`와 `divisor`를 가지고 몫을 구한다.

단순하게 하자면 그냥 `dividend`에서 `divisor`을 반복해서 빼면서 숫자를 세면 된다. 하지만 이렇게 할 경우 시간 복잡도가 `O(n)`이 되기 때문에, 비트 연산자 `<<=`를 사용하여 `divisor`를 `2`만큼 비트 이동하면서 `dividend`에서 `divisor`를 뺀다. 역시 카운트도 `2`만큼 비트 이동하면서 증가시킨다. 이를 반복하면 `O(log n)`의 시간 복잡도를 가지게 할 수 있다.
