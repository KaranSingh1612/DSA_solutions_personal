#brute force
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        default = ListNode()
        temp = head
        my_set = set()
        while temp is not None:
            if temp in my_set:
                return temp
            my_set.add(temp)
            temp = temp.next
        return None

#optimal solution
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast
        return None