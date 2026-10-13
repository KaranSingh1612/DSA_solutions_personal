class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0
        dummy = ListNode()
        curr = dummy
        
        while l1 and l2:
            total = l1.val + l2.val + carry
            if total < 10:
                curr.next = ListNode(total)
                curr = curr.next
                carry = 0
            else:
                curr.next = ListNode(total - 10)
                curr = curr.next
                carry = 1
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            total = l1.val + carry
            if total < 10:
                curr.next = ListNode(total)
                curr = curr.next
                carry = 0
            else:
                curr.next = ListNode(total - 10)
                curr = curr.next
                carry = 1
            l1 = l1.next
            
        while l2:
            total = l2.val + carry
            if total < 10:
                curr.next = ListNode(total)
                curr = curr.next
                carry = 0
            else:
                curr.next = ListNode(total - 10)
                curr = curr.next
                carry = 1
            l2 = l2.next
            
        if carry > 0:
            curr.next = ListNode(carry)
            
        return dummy.next