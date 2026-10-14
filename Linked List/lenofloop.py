#very high space comlpexity
class Solution:
    def lengthOfLoop(self, head):
        my_dict = {}
        temp = head
        count = 0
        while temp is not None:
            if temp not in my_dict:
                my_dict[temp] = count  # Fixed: use variable temp as key
                count += 1
                temp = temp.next
            else:
                return count - my_dict[temp]  # Fixed: lookup node temp
        return 0

#optimal solution
class Solution:
    def lengthOfLoop(self, head):
        slow = head
        fast = head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0