from typing import Optional
import math


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def setNext(self, next):
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print("start")

        if head is None:
            return head

        if head.next == None:
            return head

        total_elements = 1
        current = head.val
        next = head.next

        while next is not None:
            total_elements += 1
            current = next.val
            next = next.next

        middle_position = 0
        if total_elements % 2 == 0:
            middle_position = (total_elements / 2) + 1
        else:
            middle_position = math.ceil(total_elements / 2)

        print("total elements: ", total_elements)
        print("middle point: ", middle_position)
        
        current = head
        cur_pos = 1
        result = None
        while current is not None:
            if middle_position == cur_pos:
                result = current
                break
            else:
                cur_pos += 1
                current = current.next
                
        return result


if __name__ == "__main__":
    solution = Solution()

    node4 = ListNode(4)
    node3 = ListNode(3)
    node3.setNext(node4)

    node2 = ListNode(2)
    node2.setNext(node3)

    node1 = ListNode(1)
    node1.setNext(node2)
    
    node0 = ListNode(0)
    node0.setNext(node1)

    print(solution.middleNode(node0))
