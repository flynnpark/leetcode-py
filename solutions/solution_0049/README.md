# 0049. Group Anagrams

Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#### Example 1:

<pre><code><strong>Input:</strong> ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]</code></pre>

#### Example 3:

<pre><code><strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]</code></pre>

#### Constraints:

- <code>1 <= strs.length <= 10<sup>4</sup></code>
- <code>0 <= strs[i].length <= 100</code>
- <code>strs[i]</code> consists of lower-case English letters.

## 해결 방법

입력값으로 단어의 리스트가 주어지는데, 이 리스트는 애너그램의 그룹이며, 함수의 결과값은 주어진 단어들을 애너그램 단위로 묶은 결과를 반환해야 한다.

먼저 애너그램이란 어떤 단어/문장의 문자를 재배열하여 다른 뜻을 가진 단어/문장으로 바꾸는 것을 말한다. 예시에 주어진 `eat`의 경우 `ate`나 `tea`와 같은 단어로 바꿔질 수 있기 때문에 이 세 단어는 같은 애너그램 그룹이라고 볼 수 있다.

이 문제를 해결하기 위해서는 먼저 주어진 단어가 애너그램인지 파악을 해야 하는데, 이는 주어진 단어를 문자 단위로 정렬하여 같은 값을 가질 경우로 간단하게 확인할 수 있다. 그리고 `dict`를 사용하여 같은 애너그램 그룹일 경우엔 묶어주면 된다. 조건에 입력 값은 무조건 소문자라고 하였기 때문에 대소문자 처리는 따로 안 해주어도 된다.

문제 자체는 나름 쉽게 풀 수 있었으나 테스트 코드를 작성하는 데에 고생을 좀 했다. 예시로 주어진 값과 실제로 함수를 실행시켜 나온 값이 내용은 맞았지만 순서가 달랐기 때문이다. 몇 가지 방법을 실험해 보다가 결국 테스트 코드 내에서 각 문제에 해당하는 2차원 리스트 자체를 전부 다 정렬해버리는 함수를 만들어 실제 결과값과 예상되는 결과값 모두 정렬해 버린 후 같은지 확인하도록 하는 테스트 코드를 작성하였다.

순서가 다른 2차원 리스트의 비교는 처음 해보는 거였는데, 공부를 조금 더 해봐야할 듯 하다. 영 찝찝하네.
