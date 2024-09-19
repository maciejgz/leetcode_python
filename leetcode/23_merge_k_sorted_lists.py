
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)           

         
         
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        
        all_empty = True
        for i in range(len(lists)):
            if lists[i] is not None and isinstance(lists[i], ListNode):
                all_empty = False
                break
                
        if all_empty:
            return None
        
        begin = None
        last_head = None
        
        some_elements_left = True
        
        current_head_value = 10000;
        
        ## find lowest element
        lowest_key = 0
        for i in range(len(lists)):
            if lists[i] is not None and isinstance(lists[i], ListNode):
                if lists[i].val < current_head_value:
                    current_head_value = lists[i].val
                    lowest_key = i;
                
        ## assign lowest element to head and current head value
        begin = lists[lowest_key];
        last_head = lists[lowest_key]
        lists[lowest_key] = begin.next
        
        while some_elements_left:
            some_elements_left = False
            current_lowest_value = 100000
            lowest_key = -1
            
            ## find lowest val in a run 
            for i in range(len(lists)):
                if lists[i] is not None and isinstance(lists[i], ListNode):
                    some_elements_left = True
                    if lists[i].val < current_lowest_value:
                        lowest_key = i
                        current_lowest_value = lists[i].val
                        
            if lowest_key == -1 or some_elements_left == False:
                break
            else:
                ## assign lowest key to the last head next value
                last_head.next = lists[lowest_key]
                lists[lowest_key] = last_head.next.next
                last_head = last_head.next
                
        return begin
                
        
        

if __name__ == "__main__":
    solution = Solution();
    
    node15 = ListNode(5, None)
    node14 = ListNode(4, node15)
    node11 = ListNode(1, node14)
    
    node24 = ListNode(4, None)
    node23 = ListNode(3, node24)
    node21 = ListNode(1, node23)
    
    node36 = ListNode(6, None)
    node32 = ListNode(2, node36)
    
    print(solution.mergeKLists([node11, node21, node32]));
    print(solution.mergeKLists([]));
    print(solution.mergeKLists([[]]));