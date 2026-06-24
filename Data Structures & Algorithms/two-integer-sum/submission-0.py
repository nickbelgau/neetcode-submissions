class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from typing import List
        
        index_by_value = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_by_value:
                j = index_by_value[complement]
                return [j, i] if j < i else [i, j]
            index_by_value[num] = i