from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        
        if l1 is None:
            l1, l2 = l2, l1
        
        if l1 is not None and l2 is not None and l1.val > l2.val:
            l1, l2 = l2, l1
        
        # ensure that l1 < l2 initially
        head = ListNode(l1.val)
        l1 = l1.next
        pre_node = head
        while not (l1 is None and l2 is None):
            if l1 is None:
                new_node = ListNode(l2.val)
                pre_node.next = new_node
                pre_node = new_node
                l2 = l2.next
            elif l2 is None:
                new_node = ListNode(l1.val)
                pre_node.next = new_node
                pre_node = new_node
                l1 = l1.next
            elif l1.val >= l2.val:
                new_node = ListNode(l2.val)
                pre_node.next = new_node
                pre_node = new_node
                l2 = l2.next
            elif l1.val < l2.val:
                new_node = ListNode(l1.val)
                pre_node.next = new_node
                pre_node = new_node
                l1 = l1.next

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
    l1s = [[2], [1, 2, 4], [], []]
    l2s = [[1], [1, 3, 4], [], [0]]
    for l1, l2 in zip(l1s, l2s):
        h1, h2 = arrToList(l1), arrToList(l2)
        ans = sol.mergeTwoLists(h1, h2)
        print(listToarr(ans))