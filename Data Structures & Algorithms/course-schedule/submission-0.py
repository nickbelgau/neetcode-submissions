class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        prereq_list = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            prereq_list[course].append(prerequisite)

        visiting = set()
        completed = set()

        def can_finish_course(course: int) -> bool:
            if course in visiting:
                return False
            if course in completed:
                return True

            visiting.add(course)

            for prerequisite in prereq_list[course]:
                if not can_finish_course(prerequisite):
                    return False

            visiting.remove(course)
            completed.add(course)
            return True

        for course in range(numCourses):
            if not can_finish_course(course):
                return False

        return True