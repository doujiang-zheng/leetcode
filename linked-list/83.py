from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        p1 = head
        p2 = head.next
        while p2 is not None:
            if p2.val == p1.val:
                p1.next = p2.next
                p2 = p2.next
            else:
                p1 = p2
                p2 = p2.next
        return head


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
    heads = [[1, 1, 2], [1, 1, 2, 3, 3]]
    for head in heads:
        head = arrToList(head)
        ans = sol.deleteDuplicates(head)
        print(listToarr(ans))