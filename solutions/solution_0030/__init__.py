from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_length = len(words[0])
        word_count = Counter(words)
        result = []

        for i in range(word_length):
            left = i
            current_count: defaultdict[str, int] = defaultdict(int)
            used_word_count = 0

            for j in range(i, len(s) - word_length + 1, word_length):
                word = s[j : j + word_length]

                if word not in word_count:
                    left = j + word_length
                    current_count.clear()
                    used_word_count = 0
                    continue

                used_word_count += 1
                current_count[word] += 1

                while current_count[word] > word_count[word]:
                    current_count[s[left : left + word_length]] -= 1
                    left += word_length
                    used_word_count -= 1

                if used_word_count == len(words):
                    result.append(left)

        return result


"""풀이 설명
이 문제는 주어진 문자열에서 주어진 단어들이 연속해서 등장하는 인덱스를 찾는 문제입니다.
대략적인 풀이 방법은 다음과 같습니다.

1. 주어진 단어들을 Counter로 세어둡니다.
2. 단어의 길이를 구합니다.
3. 단어의 길이만큼 반복문을 돌면서 시작 인덱스를 바꿔가며 단어들을 찾습니다.
4. 시작 인덱스부터 단어의 길이만큼 문자열을 자릅니다.
5. 자른 문자열이 주어진 단어들 중에 있는지 확인합니다.
6. 자른 문자열이 주어진 단어들 중에 없다면 시작 인덱스를 다음 인덱스로 바꾸고 다시 시작합니다.
7. 자른 문자열이 주어진 단어들 중에 있다면 현재 단어의 개수를 세어둡니다.
8. 현재 단어의 개수가 주어진 단어들의 개수와 같다면 결과에 시작 인덱스를 추가합니다.
9. 현재 단어의 개수가 주어진 단어들의 개수보다 크다면 시작 인덱스를 다음 인덱스로 바꾸고 다시 시작합니다.
10. 결과를 반환합니다.

이 문제를 풀이한 방법은 '슬라이딩 윈도우'라는 방법을 사용했습니다.
슬라이딩 윈도우는 특정 범위를 이동하면서 문제를 해결하는 방법입니다.
이 문제에서는 단어의 길이만큼 인덱스를 이동하면서 단어들을 찾았습니다.
"""
