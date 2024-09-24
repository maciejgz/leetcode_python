from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if intervals is None or len(intervals) == 0:
            return None

        result = []
        
        intervals.sort(key=lambda x: x[0])

        current_start = intervals[0][0]
        current_finish = intervals[0][1]

        for interval in intervals:
            if (
                (interval[0] >= current_start and interval[0] <= current_finish)
                or (interval[1] >= current_start and interval[1] <= current_finish)
                or (interval[0] <= current_start and interval[1] >= current_finish)
            ):
                if interval[0] < current_start:
                    current_start = interval[0]

                if interval[1] > current_finish:
                    current_finish = interval[1]
            else:
                result.append([current_start, current_finish])
                current_start = interval[0]
                current_finish = interval[1]

        result.append([current_start, current_finish])

        return result


if __name__ == "__main__":
    sol = Solution()
    # print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    # print(sol.merge([[1, 4], [4, 5]]))
    print(sol.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
