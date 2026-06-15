class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        path = []

        def dfs(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path.copy())
                return

            for index in range(start, len(nums)):
                num = nums[index]
                if num > remaining:
                    break

                path.append(num)
                dfs(index, remaining - num)  # reuse allowed, so stay at index
                path.pop()

        dfs(0, target)
        return result