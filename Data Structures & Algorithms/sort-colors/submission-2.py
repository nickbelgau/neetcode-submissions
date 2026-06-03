class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_counts = [0, 0, 0]
        # color_counts = [0] * (max(nums) + 1)

        for num in nums:
            color_counts[num] += 1

        index = 0

        for color in range(len(color_counts)):
            for _ in range(color_counts[color]):
                nums[index] = color
                index += 1