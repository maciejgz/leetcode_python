from typing import List
import unittest


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        This method calculates the minimum intervals needed to execute all tasks with the given cooldown period.
        
        Steps:
        1. Count the frequency of each task using a dictionary.
        2. Find the maximum frequency of any task.
        3. Count how many tasks have this maximum frequency.
        4. Calculate the number of parts (part_count) and the length of each part (part_length).
        5. Calculate the number of empty slots (empty_slots) in the schedule.
        6. Calculate the number of available tasks that can fill these empty slots.
        7. Calculate the number of idle slots (idles) that remain after filling available tasks.
        8. Return the total time which is the sum of the length of tasks and idle slots.
        """
        if not tasks:
            return 0
        
        task_map = {}
        for task in tasks:
            if task in task_map:
                task_map[task] += 1
            else:
                task_map[task] = 1
        
        max_count = max(task_map.values())
        max_count_tasks = list(task_map.values()).count(max_count)
        
        part_count = max_count - 1
        part_length = n - (max_count_tasks - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_count * max_count_tasks
        idles = max(0, empty_slots - available_tasks)
        
        return len(tasks) + idles
        
    
    def leastIntervalOptimized(self, tasks: List[str], n: int) -> int:
        task_count = [0] * 26
        for task in tasks:
            task_count[ord(task) - ord("A")] += 1

        task_count.sort()
        max_task_count = task_count[-1] - 1
        idle_slots = max_task_count * n

        for i in range(24, -1, -1):
            idle_slots -= min(task_count[i], max_task_count)

        return len(tasks) + max(0, idle_slots)
        
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_leastInterval_example1(self):
        tasks = ["A","A","A","B","B","B"]
        n = 2
        expected = 8
        self.assertEqual(self.solution.leastInterval(tasks, n), expected)

    def test_leastInterval_example2(self):
        tasks = ["A","A","A","B","B","B"]
        n = 0
        expected = 6
        self.assertEqual(self.solution.leastInterval(tasks, n), expected)

    def test_leastInterval_example3(self):
        tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
        n = 2
        expected = 16
        self.assertEqual(self.solution.leastInterval(tasks, n), expected)
        
    def test_leastInterval_example4(self):
        tasks = ["A","C","A","B","D","B"]
        n = 1
        expected = 6
        self.assertEqual(self.solution.leastInterval(tasks, n), expected)
        
    def test_leastInterval_example5(self):
        tasks = ["A","A","A", "B","B","B"]
        n = 3
        expected = 10
        self.assertEqual(self.solution.leastInterval(tasks, n), expected)

if __name__ == "__main__":
    unittest.main()