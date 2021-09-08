from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head
        first = head
        second = head
        while second is not None and second.next is not None:
            pre = first
            first = first.next
            second = second.next.next

        return pre, first

    def reverseList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None
        pre = head
        cur = head.next
        while cur is not None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        head.next = None
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True

        pre, mid = self.middleNode(head)
        pre.next = None
        rmid = self.reverseList(mid)
        l1 = head
        l2 = rmid
        while l1 is not None and l2 is not None:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True


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
    heads = [[1], [1, 2, 2, 1], [1, 2]]
    for head in heads:
        head = arrToList(head)
        print(sol.isPalindrome(head))