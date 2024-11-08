from typing import List
import unittest


class MyQueue:


    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self._move_in_to_out()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._move_in_to_out()
        return self.stack_out[-1]
        

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out
        
    def _move_in_to_out(self) -> None:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        

class TestMyQueue(unittest.TestCase):

    def setUp(self):
        self.queue = MyQueue()

    def test_queue_operations(self):
        self.assertTrue(self.queue.empty())
        
        self.queue.push(1)
        self.queue.push(2)
        self.assertFalse(self.queue.empty())
        
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.pop(), 1)
        self.assertEqual(self.queue.pop(), 2)
        self.assertTrue(self.queue.empty())

    def test_mixed_operations(self):
        self.queue.push(1)
        self.queue.push(2)
        self.assertEqual(self.queue.pop(), 1)
        
        self.queue.push(3)
        self.assertEqual(self.queue.peek(), 2)
        self.assertEqual(self.queue.pop(), 2)
        self.assertEqual(self.queue.pop(), 3)
        self.assertTrue(self.queue.empty())


if __name__ == "__main__":
    unittest.main()