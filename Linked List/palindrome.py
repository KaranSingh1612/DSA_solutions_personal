#Brute Force
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        stack = []
        slow = head
        fast = head
        while fast and fast.next is not None:
            stack.append(slow)
            slow = slow.next
            fast = fast.next.next
        
        if fast is not None:
            slow = slow.next
            
        while slow is not None:
            curr = stack.pop()
            if curr.val != slow.val:
                return False
            slow = slow.next
        return True

#optimal solution ( takes no extra space)
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the linked list in-place
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # Step 3: Compare the first half and the reversed second half
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True