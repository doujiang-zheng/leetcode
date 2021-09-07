from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        sent = ListNode(-1)

        p = sent
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1 is not None:
            p.next = l1
        if l2 is not None:
            p.next = l2

        return sent.next

    def getMids(self, head: Optional[ListNode]):
        if head is None:
            return head
        pre = ListNode(-1, head)
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        return pre, slow

    def mergesort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        pre, mid = self.getMids(head)
        pre.next = None
        h1 = self.mergesort(head)
        h2 = self.mergesort(mid)
        h = self.mergeTwoLists(h1, h2)
        return h

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergesort(head)


def arrToList(arr: List[int]):
    if len(arr) <= 0:
        return None

    head = ListNode(arr[0])
    node = head
    for val in arr[1:]:
        next = ListNode(val)
        node.next = next
        node = next
    return head


def listToarr(l: Optional[ListNode]):
    arr = []
    while l is not None:
        arr.append(l.val)
        l = l.next
    return arr


if __name__ == '__main__':
    sol = Solution()
    heads = [[4, 2, 1, 3], [-1, 5, 3, 4, 0], []]
    for head in heads:
        head = arrToList(head)
        ans = sol.sortList(head)
        print(listToarr(ans))