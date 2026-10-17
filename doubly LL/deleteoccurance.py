class Solution:
    def deleteAllOccurOfX(self, head, x):
        curr = head
        while curr:
            if curr.data == x:
                if curr == head:
                    head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                if curr.prev:
                    curr.prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
        return head