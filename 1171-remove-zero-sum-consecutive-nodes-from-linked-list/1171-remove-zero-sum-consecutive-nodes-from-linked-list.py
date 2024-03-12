# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        cur = head
        
        while cur:
            temp = cur.val
            j = len(nums) - 1
            deleted = False
            while j >=0:
                temp = temp + nums[j]
                if temp == 0:
                    deleted = True
                    nums = nums[:j]
                    break
                j -= 1
            if not deleted and cur.val != 0:
                nums.append(cur.val)
                    
            cur =  cur.next
        
        if not nums:
            return None
        
        head = ListNode(nums[0])
        new_cur = head
        for ele in nums[1:]:
            new_cur.next = ListNode(ele)
            new_cur = new_cur.next

        return head
        
            
            