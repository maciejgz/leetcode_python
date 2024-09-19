# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        currentNode1 = list1
        currentNode2 = list2
        head = None
        if list1.val <= list2.val:
            head = list1
            currentNode1 = list1.next
        else:
            head = list2
            currentNode2 = list2.next

        lastNode = head
        while True:
            if currentNode1 is None and currentNode2 is None:
                break

            if currentNode1 is not None and currentNode2 is not None:
                if currentNode1.val <= currentNode2.val:
                    lastNode.next = currentNode1
                    lastNode = currentNode1
                    currentNode1 = currentNode1.next
                    
                else:
                    lastNode.next = currentNode2
                    lastNode = currentNode2
                    currentNode2 = lastNode.next
                    
            else:
                if currentNode1 is None:
                    lastNode.next = currentNode2
                    lastNode = currentNode2
                    currentNode2 = lastNode.next
                    if lastNode is not None and lastNode.next is not None:
                        currentNode2 = lastNode.next
                    else:
                        currentNode2 = None

                if currentNode2 is None:
                    lastNode.next = currentNode1
                    lastNode = currentNode1
                    if lastNode is not None and lastNode.next is not None:
                        currentNode1 = lastNode.next
                    else:
                        currentNode1 = None
                        

        return head


if __name__ == "__main__":
    solution = Solution()

    node14 = ListNode(4, None)
    node13 = ListNode(3, node14)
    node12 = ListNode(2, node13)
    node11 = ListNode(1, node12)

    node26 = ListNode(6, None)
    node22 = ListNode(2, node26)

    print(solution.mergeTwoLists(node11, node22))
