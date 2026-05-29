from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point: List[int]) -> float:
            return sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)

        def partition(left: int, right: int) -> int:
            pivot_distance = distance(points[right])
            boundary = left

            for i in range(left, right):
                if distance(points[i]) <= pivot_distance:
                    points[boundary], points[i] = points[i], points[boundary]
                    boundary += 1

            points[boundary], points[right] = points[right], points[boundary]
            return boundary

        def quick_select(left: int, right: int) -> None:
            if left >= right:
                return

            pivot_index = partition(left, right)

            if pivot_index == k - 1:
                return
            if pivot_index > k - 1:
                quick_select(left, pivot_index - 1)
            else:
                quick_select(pivot_index + 1, right)

        quick_select(0, len(points) - 1)
        return points[:k]