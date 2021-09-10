# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
       pass

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
       pass

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
       pass

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        que = []
        for el in nestedList:
            que.extend(self.dfs(el))
        self.que = que
        self.cur = 0

    def dfs(self, num: NestedInteger):
        if num.isInteger():
            return [num]
        else:
            nums = num.getList()
            ans = []
            for el in nums:
                ans.extend(self.dfs(el))
            return ans
        
    
    def next(self) -> int:
        ans = self.que[self.cur]
        self.cur += 1
        return ans
        
    
    def hasNext(self) -> bool:
        return self.cur < len(self.que)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())