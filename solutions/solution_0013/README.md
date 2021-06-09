## 0013. [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

<pre><code>
<strong>Symbol       Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
</code></pre>

For example, `2` is written as `II` in Roman numeral, just two one's added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

#### Example 1:

<pre><code><strong>Input:</strong> s = "III"
<strong>Output:</strong> 3</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> s = "IV"
<strong>Output:</strong> 4</code></pre>

#### Example 3:

<pre><code><strong>Input:</strong> s = "IX"
<strong>Output:</strong> 9</code></pre>

#### Example 4:

<pre><code><strong>Input:</strong> s = "LVIII"
<strong>Output:</strong> 58
<strong>Explanation:</strong> L = 50, V= 5, III = 3.</code></pre>

#### Example 5:

<pre><code><strong>Input:</strong> s = "MCMXCIV"
<strong>Output:</strong> 1994
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.</code></pre>

#### Constraints:

- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

## 해결 방법

처음에는 어떻게 해야 하나 감이 잘 잡히지 않았다. 일단 문제에 쓰여진 대로 로마 숫자의 규칙을 파악해야 한다. 로마 숫자에서 큰 숫자가 보통 앞쪽에 위치하며 큰 숫자 앞에 작은 숫자가 위치할 경우엔 큰 숫자에서 작은 숫자를 뺀 값이 된다. 이러한 규칙들을 사용하여 문제를 해결하면 된다.

로마 숫자를 먼저 사전 정의 했는데, 4, 9와 같이 작은 숫자가 큰 숫자 앞에 오는 경우를 먼저 정의할 수도 있겠지만 그렇게 하기 싫어서 하나씩 비교해가기로 했다. 현재 인덱스의 숫자와 바로 이전 인덱스의 숫자를 비교하여 이전 숫자가 현재보다 작을 경우엔 큰 숫자에서 작은 숫자에 2를 곱한 값을 뺀다. 이 때 2를 곱하는 이유는 현재 인덱스의 숫자가 이전 인덱스의 숫자가 작을 경우엔 그냥 바로 현재 값을 더하기 때문이다. 예를 들어 `IV`의 경우 `I`를 먼저 더하고 난 후 `V`의 위치에서 비교를 하는데, `I`가 `V`보다 작기 때문에 2를 곱한 값을 빼는 것이다. 즉, `1 + 5 - (1 * 2)`가 되는 것.
