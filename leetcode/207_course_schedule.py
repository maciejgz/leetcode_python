from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True

            visited[course] = 1
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            visited[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.canFinish(2, [[1, 0]]))           # true
    print(obj.canFinish(2, [[1, 0], [0, 1]]))   # false
