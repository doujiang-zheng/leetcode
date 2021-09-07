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

        front = ListNode(val=-102, next=head)
        prev, curr, runner = front, front.next, front.next.next
        
        while curr is not None and curr.next is not None:
            if curr.val != prev.val and curr.val != runner.val:
                curr = curr.next
                prev = prev.next
                runner = runner.next
            else:
                while runner is not None and curr.val == runner.val:
                    runner = runner.next
                prev.next = runner
                curr = runner
                if curr is not None:
                    runner = runner.next
       
        return front.next

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
    heads = [[1, 1, 2, 3, 3], [], [1, 2, 3, 3, 4, 4, 5], [1, 1, 1, 2, 3]]
    for head in heads:
        head = arrToList(head)
        ans = sol.deleteDuplicates(head)
        print(listToarr(ans))