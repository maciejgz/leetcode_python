# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
    def __str__(self):
        result = []
        current = self
        while current is not None:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev = None
        current = head;
        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
            
        return prev
            
    
if __name__ == '__main__':
    s = Solution()
    n5 = ListNode(5, None)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    print(s.reverseList(n1))