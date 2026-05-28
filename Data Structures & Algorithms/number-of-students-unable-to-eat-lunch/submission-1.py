class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_circle = 0
        count_square = 0

        for student in students:
            if student == 0:
                count_circle += 1
            else:
                count_square += 1

        for sandwich in sandwiches:
            if sandwich == 0:
                if count_circle == 0:
                    return count_square
                count_circle -= 1
            else:
                if count_square == 0:
                    return count_circle
                count_square -= 1

        return 0
'''
instead of simulating every rotation, think:
Count how many students want 0
Count how many students want 1
Walk through the sandwiches stack from top to bottom
For each sandwich:
if nobody wants that type anymore, return how many students are left
otherwise decrement that preference count
'''