class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            n = curr.next 
            curr.next = prev
            prev = curr
            curr = n
        
        return prev