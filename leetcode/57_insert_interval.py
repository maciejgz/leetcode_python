from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if intervals is None or len(intervals) == 0:
            return [newInterval]

        intervals.sort(key=lambda x: x[0])

        result = []
        local_min = newInterval[0]
        local_max = newInterval[1]
        for i in range(len(intervals)):
            if (
                (intervals[i][0] >= local_min and intervals[i][0] <= local_max)
                or (intervals[i][1] >= local_min and intervals[i][1] <= local_max)
                or (intervals[i][0] <= local_min and intervals[i][1] >= local_max)
            ):
                if intervals[i][0] < local_min:
                    local_min = intervals[i][0]

                if intervals[i][1] > local_max:
                    local_max = intervals[i][1]

            else:
                result.append(intervals[i])
                
        result.append([local_min, local_max])
        result.sort(key=lambda x: x[0])
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1, 3], [6, 9]], [2, 5]))
    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
