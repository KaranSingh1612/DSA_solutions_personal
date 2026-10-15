class Solution:
    def reverse(self, head):
        # code here
        if head.next is None:
            return head
        curr = head
        prev = None
        while curr is not None:
            front = curr.next
            curr.next = prev
            curr.prev = front
            prev = curr
            curr = front
        return prev