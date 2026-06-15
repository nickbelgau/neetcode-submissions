class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def dfs(index: int) -> None:
            if index == len(nums):
                result.append(path.copy())  # save the current answer before the list gets reused
                return
            path.append(nums[index]) # mark the choice
            dfs(index + 1)
            path.pop()                 # undo the choice
            dfs(index + 1)
        dfs(0)
        return result