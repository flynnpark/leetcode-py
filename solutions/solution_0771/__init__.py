class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = {}
        for stone in stones:
            if stone in table:
                table[stone] += 1
            else:
                table[stone] = 1

        count = 0
        for jewel in jewels:
            if jewel in table:
                count += table[jewel]

        return count
