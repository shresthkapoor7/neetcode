from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        q = deque()
        curr = head

        while curr:
            q.append(curr)
            curr = curr.next

        dummy = ListNode()
        tail = dummy

        while q:
            tail.next = q.popleft()
            tail = tail.next

            if q:
                tail.next = q.pop()
                tail = tail.next

        tail.next = None
        head = dummy.next
        # head.val = dummy.next.val
        # head.next = dummy.next.next
