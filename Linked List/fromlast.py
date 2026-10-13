class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        slow = head
        fast = head
        
        count = 0
        while count < n:
            fast = fast.next
            count += 1
            
        # If fast is None, n equals the list length; remove the head node
        if fast is None:
            return head.next
            
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next
            
        dummy = slow.next
        slow.next = dummy.next
        del dummy
        return head