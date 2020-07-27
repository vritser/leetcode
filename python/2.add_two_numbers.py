class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 != None or l2 != None:
            a = 0 if l1 == None else l1.val
            b = 0 if l2 == None else l2.val

            sum = a + b + carry
            carry = int(sum / 10)
            curr.next = ListNode(sum % 10)
            curr = curr.next

            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next

        if carry > 0: curr.next = ListNode(carry)

        return dummy.next





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
