class Solution:
    def countBits(self, n: int) -> list[int]:
        output = [0] * (n + 1)

        for number in range(1, n + 1):
            # number >> 1 removes the rightmost bit.
            # number & 1 is 1 when the rightmost bit is set.
            output[number] = output[number >> 1] + (number & 1)

        return output