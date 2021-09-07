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
        
        # find the first non-duplicate node
        cur = head
        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                val = cur.val
                # find the next number
                while cur is not None and cur.val == val:
                    cur = cur.next
            else:
                break
        
        head = cur
        if head is None:
            return head
        pre = head
        cur = head.next
        while cur is not None:
            if cur.next is not None and cur.val == cur.next.val:
                val = cur.val
                # find the next number
                while cur is not None and cur.val == val:
                    cur = cur.next
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        # if the last one is duplicate, set pre.next = None
        # if the last one is not duplicate, pre == the last one
        pre.next = cur
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
    heads = [[], [1, 2, 3, 3, 4, 4, 5], [1, 1, 1, 2, 3]]
    for head in heads:
        head = arrToList(head)
        ans = sol.deleteDuplicates(head)
        print(listToarr(ans))