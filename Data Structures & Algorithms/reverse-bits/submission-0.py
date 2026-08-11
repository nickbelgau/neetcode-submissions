class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            # Take n's rightmost bit and append it to result.
            result = (result << 1) | (n & 1)

            # Remove n's rightmost bit.
            n >>= 1

        return result