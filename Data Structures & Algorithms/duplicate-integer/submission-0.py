class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False