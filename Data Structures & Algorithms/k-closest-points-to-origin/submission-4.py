from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = sqrt(x**2 + y**2)
            # min heap with priority tuples
            heapq.heappush(heap, (dist, [x, y]))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result