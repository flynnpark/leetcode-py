class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters = []
        digits = []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda letter_log: (letter_log.split()[1:], letter_log.split()[0]))
        return letters + digits
