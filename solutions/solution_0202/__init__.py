class Solution:
    def isHappy(self, n: int) -> bool:
        current_number = n
        checked_numbers = {}

        while True:
            number_sum = 0
            for i in str(current_number):
                number_sum += int(i) ** 2

            if number_sum == 1:
                return True

            if number_sum in checked_numbers:
                return False

            checked_numbers[number_sum] = True
            current_number = number_sum


"""풀이 설명
이 문제는 주어진 숫자가 '행복한 숫자'인지 판별하는 문제입니다. 행복한 숫자는 다음과 같은 규칙을 따릅니다.
1. 주어진 숫자의 각 자리수를 제곱한 값을 더합니다.
2. 위의 과정을 반복합니다.
3. 숫자가 1이 될 때까지 반복합니다.
4. 숫자가 1이면 '행복한 숫자'이고, 1이 아니면 '행복한 숫자'가 아닙니다.
5. 숫자가 1이 아니더라도 반복되는 숫자가 있으면 '행복한 숫자'가 아닙니다.

대략적인 풀이 방법은 다음과 같습니다.
1. 주어진 숫자를 변수에 저장합니다.
2. 반복문을 돌면서 각 자리수를 제곱한 값을 더합니다.
3. 더한 값이 1이면 '행복한 숫자'이므로 True를 반환합니다.
4. 더한 값이 이미 확인한 숫자라면 False를 반환합니다.
5. 더한 값이 1이 아니라면 확인한 숫자로 추가하고 다시 반복합니다.
6. 결과를 반환합니다.
"""
