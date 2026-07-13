# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        mem = ListNode()
        memCurr = mem
        memTracker = 0

        current = head

        while current:
            print("state:", current.val)
            memCurr.next = current
            memTracker += 1
            if memTracker > n + 1:
                print("forgetting", mem.val)
                mem = mem.next #forgetting first pointer to maintain tracker up to n + 1 nodes

            memCurr = memCurr.next
            current = current.next


        if memTracker == n: #accounting for when n = length of LL
            return head.next
        
        mem = mem.next #removing empty start
        mem.next = mem.next.next  #then skipping node
        
        return head

        
        