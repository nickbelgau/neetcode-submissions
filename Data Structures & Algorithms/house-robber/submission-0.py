class Solution:
    def rob(self, nums: List[int]) -> int:
        # previous_two = best total up through house i - 2
        # previous_one = best total up through house i - 1
        previous_two = 0
        previous_one = 0

        for money in nums:
            rob_current = previous_two + money
            skip_current = previous_one

            previous_two = previous_one
            previous_one = max(rob_current, skip_current)

        return previous_one