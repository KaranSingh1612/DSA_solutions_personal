#brute force takes a lot more space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        my_set = set()
        while temp is not None:
            if temp not in my_set:
                my_set.add(temp)
                temp = temp.next
            elif temp in my_set:
                return True
        return False

# tortoise and hare approach
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False