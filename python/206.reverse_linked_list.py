
from typedef.listnode import ListNode

# https://leetcode.com/problems/reverse-linked-list
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = None
        while head:
            next = head.next
            head.next = dummy
            dummy = head
            head = next
        return dummy

    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = self.reverseList2(head.next)
        head.next.next = head
        head.next = None

        return prev
