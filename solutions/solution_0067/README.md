# 0067. [Add Binary](https://leetcode.com/problems/add-binary/)

Given two binary strings `a` and `b`, return _their sum as a binary string_.

#### Example 1:

<pre><code><strong>Input:</strong> a = "11", b = "1"
<strong>Output:</strong> "100"</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> a = "1010", b = "1011"
<strong>Output:</strong> "10101"</code></pre>

#### Constraints:

- `1 <= a.length, b.length <= 10<sup>4</sup>`
- `a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.

## 해결 방법

문자열로 주어지는 두 이진수를 더해서 다시 이진수 문자열로 반환하는 문제이다. 간단하게 `int(num, 2)`를 통해 10진수로 변환하여 덧셈을 진행한 후, `format(num, 'b')`를 통해 다시 이진수로 변환해줍니다. `bin(num)`을 사용해도 되지만, `0b` 접두사가 붙어 추가적인 처리를 해주어야 하므로 `format` 함수를 사용했습니다.
