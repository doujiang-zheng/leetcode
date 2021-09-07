from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode],
                  x: int) -> Optional[ListNode]:
        less = ListNode(-1)
        large = ListNode(-1)

        cur = head
        h1 = less
        h2 = large
        while cur is not None:
            if cur.val < x:
                h1.next = cur
                h1 = h1.next
            else:
                h2.next = cur
                h2 = h2.next
            cur = cur.next
        h1.next = large.next
        h2.next = None
        return less.next


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
    heads = [[], [2, 1], [1, 4, 3, 2, 5, 2], [2, 1]]
    xs = [1, 0, 3, 2]
    for head, x in zip(heads, xs):
        head = arrToList(head)
        ans = sol.partition(head, x)
        print(listToarr(ans))