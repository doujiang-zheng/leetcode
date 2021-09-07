from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: 
                break

        # no cycle
        if fast is None or fast.next is None:
            return None

        cnt = 0 # cycle length
        while True:
            slow = slow.next
            fast = fast.next.next
            cnt += 1
            if fast == slow:
                break
        
        p1 = head
        p2 = head
        # get p2 cnt-1 step ahead of p1
        for _ in range(cnt - 1):
            p2 = p2.next
        
        while p2.next != p1:
            p1 = p1.next
            p2 = p2.next
        return p1


def arrToList(arr: List[int], pos: int):
    if len(arr) <= 0:
        return None

    head = ListNode(arr[0])
    node = head
    insert = None
    for i, val in enumerate(arr[1:]):
        next = ListNode(val)
        if i + 1 == pos:
            insert = next
        node.next = next
        node = next
    
    if insert is None:
        insert = head
    if pos >= 0:
        node.next = insert
    return head


def listToarr(l: Optional[ListNode]):
    visited = set()
    arr = []
    while l is not None and l not in visited:
        arr.append(l.val)
        visited.add(l)
        l = l.next
    return arr


if __name__ == '__main__':
    sol = Solution()
    heads = [[], [1], [1, 2], [3, 2, 0, -4], [1, 2], [1]]
    poss = [0, 0, 1, 1, 0, -1]
    for head, pos in zip(heads, poss):
        head = arrToList(head, pos)
        ans = sol.detectCycle(head)
        print(listToarr(ans))