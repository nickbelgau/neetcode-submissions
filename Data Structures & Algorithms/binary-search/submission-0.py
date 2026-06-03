class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search is Ologn for sorted arrays
        # uses 2 pointers
        # calc the middle index, compare target to middle,
        # move L or R pointer to middle, repeat
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
