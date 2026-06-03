class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed: int) -> bool:
            hours_needed = 0
            for pile in piles:
                # add number of hours needed for that pile
                # add an extra hour if there's a remainder
                hours_needed += pile // speed
                if pile % speed != 0:
                    hours_needed += 1
            return hours_needed <= h

        min_speed = 1
        max_speed = max(piles) # largest speed is size of the largest pile since 1 pile per hour

        while min_speed < max_speed:
            mid = (min_speed + max_speed) // 2
            if can_finish(mid):
                max_speed = mid
            else:
                min_speed = mid + 1
        return min_speed