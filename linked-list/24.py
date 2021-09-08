from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        sent = ListNode(-1, head)
        pre = sent
        p1 = sent.next
        p2 = head.next
        while p1 is not None and p2 is not None:
            if p2.next is None:
                p1_next, p2_next = p2.next, None
            else:
                p1_next, p2_next = p2.next, p2.next.next
            pre.next = p2
            p1.next = p2.next
            p2.next = p1
            pre = p1
            p1, p2 = p1_next, p2_next

        return sent.next


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
    heads = [[1, 2, 3], [1, 2, 3, 4], [], [1]]
    for head in heads:
        head = arrToList(head)
        ans = sol.swapPairs(head)
        print(listToarr(ans))