## 0007. [Reverse Integer](https://leetcode.com/problems/reverse-integer)

Given a signed 32-bit integer `x`, return `x` _with its digits reversed_. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2<sup>31</sup>, 2<sup>31</sup> - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

#### Example 1:

<pre><code><strong>Input:</strong> x = 123
<strong>Output:</strong> 321</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> x = -123
<strong>Output:</strong> -321</code></pre>

#### Example 3:

<pre><code><strong>Input:</strong> x = 120
<strong>Output:</strong> 21</code></pre>

#### Example 4:

<pre><code><strong>Input:</strong> x = 0
<strong>Output:</strong> 0</code></pre>

#### Constraints:

- -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

## 해결 방법

32-bit로 주어지는 정수 `x`를 숫자만 거꾸로 뒤집으면 된다. 이 때, 뒤집은 숫자의 결과가 32-bit 정수형을 초과할 경우엔 0으로 반환해야 한다.

큰 어려움 없이 `x`를 문자형으로 만들고, 음수일 땐 부호를 제외한 부분만 뒤집고, 양수일 땐 그냥 다 뒤집어버린 후 `int`로 정수로 바꿔주면 된다. `x`가 음수인 경우에만 부호를 붙여서 바꿔준다. 마지막으로 결과값이 -2<sup>31</sup>보다 작거나 2<sup>31</sup>-1보다 클 경우엔 0을 반환해 준다.
