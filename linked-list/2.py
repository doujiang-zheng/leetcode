from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        pre = root
        inc = 0
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + inc
            inc = val // 10
            node = ListNode(val % 10)
            pre.next = node
            pre = node
            l1 = l1.next
            l2 = l2.next

        if l1 is None and l2 is not None:
            l1 = l2        
        while l1 is not None:
            val = l1.val + inc
            inc = val // 10
            node = ListNode(val % 10)
            pre.next = node
            pre = node
            l1 = l1.next
        
        if inc > 0:
            node = ListNode(inc)
            pre.next = node
            pre = node
        return root.next


if __name__ == '__main__':
    pass