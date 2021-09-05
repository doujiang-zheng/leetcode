import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class CompareNode:
    def __init__(self, val: int, ptr: ListNode) -> None:
        self.val = val
        self.ptr = ptr

    def __repr__(self):
        return 'Node value {}'.format(self.val)
    
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        que = []
        for l in lists:
            if l is not None:
                heapq.heappush(que, CompareNode(l.val, l))

        if len(que) <= 0:
            head = None            
        else:
            comp_node = heapq.heappop(que)
            val, node = comp_node.val, comp_node.ptr
            head = ListNode(val)
            if node.next is not None:
                heapq.heappush(que, CompareNode(node.next.val, node.next))
        
        pre_node = head
        while len(que) > 0:
            comp_node = heapq.heappop(que)
            val, node = comp_node.val, comp_node.ptr
            new_node = ListNode(val)
            if node.next is not None:
                heapq.heappush(que, CompareNode(node.next.val, node.next))
            pre_node.next = new_node
            pre_node = new_node
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


def arrToLists(arrs: List[List[int]]):
    ls = []
    for arr in arrs:
        ls.append(arrToList(arr))
    return ls


def listToarr(l: Optional[ListNode]):
    arr = []
    while l is not None:
        arr.append(l.val)
        l = l.next
    return arr

if __name__ == '__main__':
    sol = Solution()
    lists = [[[1, 4, 5], [1, 3, 4], [2, 6]], [], [[]]]
    for l in lists:
        ls = arrToLists(l)
        ans = sol.mergeKLists(ls)
        print(ans)