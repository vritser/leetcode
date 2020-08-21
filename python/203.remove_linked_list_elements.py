from typedef.listnode import ListNode

# https://leetcode.com/problems/remove-linked-list-elements
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next

        dummy = head
        prev = head

        while dummy:
            if val == dummy.val:
                prev.next = dummy.next
            else:
                prev = dummy
                dummy = dummy.next

        return head

    def removeElements2(self, head: ListNode, val: int) -> ListNode:
        if not head: return head
        head.next = self.removeElements2(head.next, val)
        return head.next if head.val == val else head
