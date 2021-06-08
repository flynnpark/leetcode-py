## 0009. [Palindrom number](https://leetcode.com/problems/palindrome-number/)

Given an integer `x`, return `true` if `x` is palindrome integer.

An integer is a **palindrome** when it reads the same backward as forward. For example, `121` is palindrome while `123` is not.

#### Example 1:

<pre><code><strong>Input:</strong> x = 121
<strong>Output:</strong> true</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.</code></pre>

#### Example 3:

<pre><code><strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.</code></pre>

#### Example 4:

<pre><code><strong>Input:</strong> x = -101
<strong>Output:</strong> false</code></pre>

#### Constraints:

- `-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1`

## 해결 방법

팰린드롬 문제인제, 이번엔 숫자다. 하지만 입력값이 음수일 경우엔 예시에서 `False`가 나오므로 그냥 문자열로 바꾼 후 뒤집어서 비교만 해주면 된다.
