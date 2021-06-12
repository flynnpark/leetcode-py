# 0014. [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

#### Example 1:

<pre><code><strong>Input:</strong> strs = ["flower","flow","flight"]
<strong>Output:</strong> "fl"</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> strs = ["dog","racecar","car"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no common prefix among the input strings.</code></pre>

#### Constraints:

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lower-case English letters.

## 해결 방법

주어진 다수의 문자열 중에서 문자의 처음부터 가장 긴 접두사를 찾는 문제이다. 접두사이기 때문에 처음 시작 지점부터 가장 긴 중복 문자열만 찾으면 된다. 처음엔 당연히 for문을 사용해서 해결할 방법을 찾았으나 하던 도중 2중 for문을 사용하게 되어 다른 방법을 찾게 되었다. 2개 가지 이상의 문자열을 어떻게 한 번에 비교할 수 있을까 하다가 내장 함수 zip을 이용하여 각 문자열의 n번째 문자를 가져오게 하였고, 중복을 허용하지 않는 set 자료형의 성격을 이용해 n번째 문자들의 중복 여부를 사용했다. 접두사이기 때문에 한 번이라도 완벽히 일치하지 않을 경우 break을 통해 for문을 빠져나온다. 아직 파이썬 내장 함수와 특징들에 대해 모르는 게 많은 듯 하다. 분발해야지.
