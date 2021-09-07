from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return 'val: {}'.format(self.val)

class Solution:
    def getMidNode(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
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

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return None
        mid = self.getMidNode(head)
        rmid = self.reverseList(mid)
        l1 = head
        l2 = rmid
        while l1 is not None and l2 is not None:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            if l2.next is not None:
                l2.next = l1_next
            l1 = l1_next
            l2 = l2_next


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
    heads = [[1, 2, 3, 4], [1, 2, 3, 4, 5]]
    for head in heads:
        head = arrToList(head)
        sol.reorderList(head)
        print(listToarr(head))