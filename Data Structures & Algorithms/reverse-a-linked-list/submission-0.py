# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        mem = None
        prev = None
        while current != None:
            mem = current.next
            current.next = prev
            prev = current
            
            if mem == None: break
            current = mem

        return current

    

    

            
        