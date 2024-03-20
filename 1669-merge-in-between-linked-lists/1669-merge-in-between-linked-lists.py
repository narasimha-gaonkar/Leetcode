# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        cur1 = list1
        end_pointer = list1
        a = a-1
        while cur1 and end_pointer and (a > 0 or b > 0):
            if a > 0:
                cur1 = cur1.next
                a-=1
            if b > 0:
                end_pointer = end_pointer.next
                b -= 1
        
        
        cur1.next = list2
        
        list2_end_pointer  = list2
        while cur1 and cur1.next:
            
            cur1 = cur1.next
        cur1.next = end_pointer.next
        
        return list1
            