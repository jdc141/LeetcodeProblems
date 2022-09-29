# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, middle, count , findVal = head, head, 0, 0
        while curr:
            curr = curr.next
            count += 1
        if count % 2 == 0:
            findVal = (count // 2) 
        else:
            findVal = count // 2
        
        for i in range(findVal):
            middle = middle.next
        
        return middle
        