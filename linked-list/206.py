from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pre, cur = head, head.next
        
        while cur is not None:
            nxt_cur = cur.next
            cur.next = pre
            pre = cur
            cur = nxt_cur
        head.next = None
        return pre


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
    heads = [[1, 2, 3, 4, 5], [1, 2], []]
    for head in heads:
        head = arrToList(head)
        ans = sol.reverseList(head)
        print(listToarr(ans))