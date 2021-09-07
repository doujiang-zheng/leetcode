from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        pre = head
        p1 = head
        p2 = head  # ahead of p1 of n-step
        for i in range(n):
            p2 = p2.next
        while p2 is not None:
            pre = p1
            p1 = p1.next
            p2 = p2.next
        
        if p1 == head:
            head = p1.next
        else:
            pre.next = p1.next

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
    heads = [[1, 2, 3, 4, 5], [1], [1, 2]]
    ns = [2, 1, 1]
    for head, n in zip(heads, ns):
        head = arrToList(head)
        ans = sol.removeNthFromEnd(head, n)
        print(listToarr(ans))