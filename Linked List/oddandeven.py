class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        odd = head
        if odd == None:
            return odd
        even = head.next
        even_head = even
        while even and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return head