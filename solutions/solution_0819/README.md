# 0819. [Most Common Word](https://leetcode.com/problems/most-common-word)

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is **guaranteed** there is **at least one word** that is not banned, and that the answer is unique.

The words in paragraph are **case-insensitive** and the answer should be returned in **lowercase**.

#### Example 1:

<pre><code><strong>Input:</strong> paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
<strong>Output:</strong> "ball"
<strong>Explanation:</strong>
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> paragraph = "a.", banned = []
<strong>Output:</strong> "a"</code></pre>

#### Constraints:

- `1 <= paragraph.length <= 1000`
- paragraph consists of English letters, space `' '`, or one of the symbols: `"!?',;."`.
- `0 <= banned.length <= 100`
- `1 <= banned[i].length <= 10`
- `banned[i]` consists of only lowercase English letters.

## 해결 방법

금지된 단어를 제외하고 제일 많이 사용된 단어를 반환하는 문제이다. 조건이 어렵지 않기 때문에 모든 특수문자를 공백으로 치환한 이후 `dict`를 사용하여 각 단어가 사용된 횟수를 확인하면 된다.

여기서 `collections` 모듈의 `defaultdict` 함수를 이용하였는데, 첫 번째 인자로 `int`를 넣어 주었기 때문에 없는 키의 값을 출력할 경우 기본값이 0으로 호출되어 곧바로 `counts[word] += 1`과 같은 코드를 쓸 수 있다.

그리고 `max` 함수의 `key`로 각 `dict`의 값을 가져올 수 있도록 `counts.get` 함수로 설정해 주어 제일 많은 숫자를 가지고 있는 `counts`의 키를 반환할 수 있도록 만들어 주었다.
