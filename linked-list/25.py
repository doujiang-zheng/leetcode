from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode],
                    tail: Optional[ListNode]) -> None:
        if head is None:
            return None
        pre = head
        cur = head.next
        while pre != tail:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        head.next = None

    def reverseKGroup(self, head: Optional[ListNode],
                      k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head

        sent = ListNode(-1, head)
        pre, head, tail = sent, head, head
        while tail is not None:
            cnt = 1
            while cnt < k and tail is not None:
                tail = tail.next
                cnt += 1
            if tail is not None:
                nxt_head = tail.next
                self.reverseList(head, tail)
                pre.next = tail
                pre, head, tail = head, nxt_head, nxt_head
            else:
                pre.next = head
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
    heads = [[1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1]]
    ks = [2, 2, 3, 1, 1]
    for head, k in zip(heads, ks):
        head = arrToList(head)
        ans = sol.reverseKGroup(head, k)
        print(listToarr(ans))