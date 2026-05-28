class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]

        for student in students:
            count[student] += 1

        for sandwich in sandwiches:
            if count[sandwich] == 0:
                return count[0] + count[1]

            count[sandwich] -= 1

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