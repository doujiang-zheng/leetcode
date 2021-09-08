from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getKthFromEnd(self, head: Optional[ListNode],
                      k: int):
        p1 = head 
        p2 = head
        for _ in range(k):
            p2 = p2.next
        
        pre = head
        while p2 is not None:
            pre = p1
            p1 = p1.next
            p2 = p2.next
        return pre, p1

    def rotateRight(self, head: Optional[ListNode],
                    k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        
        cnt = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            cnt += 1

        k = k % cnt
        if k == 0:
            return head
        pre, kth = self.getKthFromEnd(head, k)
        pre.next = None
        tail.next = head
        
        return kth


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
    heads = [[1, 2, 3, 4, 5], [0, 1, 2]]
    ks = [2, 4]
    for head, k in zip(heads, ks):
        head = arrToList(head)
        ans = sol.rotateRight(head, k)
        print(listToarr(ans))