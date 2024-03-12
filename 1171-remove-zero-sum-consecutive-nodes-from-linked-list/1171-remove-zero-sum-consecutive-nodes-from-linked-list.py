# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        root = ListNode(0, head)
        summ, hmap, node = 0, {}, root
        # print(node)
        while node:
            summ += node.val
            if summ in hmap:
                prev = hmap[summ]
                tmp = prev.next
                tmp_sum = summ
                # print('Line 20', summ, hmap[summ])
                while tmp != node:
                    tmp_sum += tmp.val
                    if tmp_sum in hmap and hmap[tmp_sum] == tmp:
                        hmap.pop(tmp_sum)
                    tmp = tmp.next
                prev.next = node.next
                node = prev
            else:
                hmap[summ] = node
            node = node.next
        return root.next
        
        
        
        
        ###Working code
        
        
        #         nums = []
#         cur = head
        
#         while cur:
#             temp = cur.val
#             j = len(nums) - 1
#             deleted = False
#             while j >=0:
#                 temp = temp + nums[j]
#                 if temp == 0:
#                     deleted = True
#                     nums = nums[:j]
#                     break
#                 j -= 1
#             if not deleted and cur.val != 0:
#                 nums.append(cur.val)
                    
#             cur =  cur.next
        
#         if not nums:
#             return None
        
#         head = ListNode(nums[0])
#         new_cur = head
#         for ele in nums[1:]:
#             new_cur.next = ListNode(ele)
#             new_cur = new_cur.next

#         return head
        
            
            