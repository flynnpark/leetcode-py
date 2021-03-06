# 0937. Reorder Data in Log Files

You are given an array of `logs`. Each log is a space-delimited string of words, where the first word is the **identifier**.

There are two types of logs:

- **Letter-logs**: All words (except the identifier) consist of lowercase English letters.
- **Digit-logs**: All words (except the identifier) consist of digits.

Reorder these logs so that:

1. The letter-logs come before all digit-logs.
2. The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
3. The digit-logs maintain their relative ordering.

Return the final order of the logs.

#### Example 1:

<pre><code><strong>Input:</strong> logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
<strong>Output:</strong> ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
<strong>Explanation:</strong>
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
<strong>Output:</strong> ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]</code></pre>

#### Constraints:

- `1 <= logs.length <= 100`
- `3 <= logs[i].length <= 100`
- All the tokens of `logs[i]` are separated by a **single** space.
- `logs[i]` is guaranteed to have an identifier and at least one word after the identifier.

## 해결 방법

문제에서 정렬 조건은 3가지이다. 문자 로그가 숫자 로그 이전에 있을 것, 문자 로그는 컨텐츠로 먼저 정렬되고 컨텐츠가 같다면 구분자로 정렬될 것, 숫자 로그는 입력 순서대로 둘 것. 모든 로그의 첫 번째 아이템은 구분자이며, 내용은 숫자 로그일 경우엔 오직 숫자로 구성되고 문자 로그의 경우엔 숫자로 구성되어 있다.

먼저 내용이 숫자인지 문자인지 구분하여 주어야 한다. `isdigit()` 함수를 이용하여 구분할 수 있으며, 숫자 로그는 내용이 모두 숫자로 구성되기 때문에 `split()` 함수를 이용하여 나온 두 번째 객체가 숫자인지 확인하는 방법으로 구분할 수 있다.

이 중 문자 로그의 경우엔 내용으로 먼저 정렬하고, 내용이 같은 경우엔 구분자로 정렬해야 한다. `sort()` 함수를 사용하면 간단한데, 정렬 조건이 한 번 꼬여져 있으므로 `lambda`를 사용하여 내용으로 먼저 정렬하도록 만들어 주었다.
