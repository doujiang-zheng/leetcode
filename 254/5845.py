from typing import List        

class Solution:
    def find(self, coord, Parent, isLeft, isRight):
        pass

    def merge(self, coord0, coord1, Parent, isLeft, isRight):
        r, c = coord0
        pr, pc = coord1
        # find which root isLeft==True or isRight==True
        # if both are False, set the one deeper as the root

        pass

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # We use union set to mark whether water covers from the left to the right.
        Parent = [[(i, j) for j in range(col)] for i in range(row)]
        lands = [[0 for _ in range(col)] for _ in range(row)]
        isLeft = [[False for _ in range(col)] for _ in range(row)]
        isRight = [[False for _ in range(col)] for _ in range(row)]

        num = len(cells)
        for i in range(num):
            coord = cells[i]
            cells[i] = [coord[0] - 1, coord[1] - 1]

        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        ans = 0
        for i in range(num):
            coord = cells[i]
            r, c = coord[0], coord[1]
            lands[r][c] = 1
            
            if c == 0:
                isLeft[r][c] = True
            if c == col - 1:
                isRight[r][c] = True

            for k in range(len(dx)):
                pr, pc = r + dx[k], c + dy[k]
                if not (0 <= pr < row and 0 <= pc < col):
                    continue
                if lands[pr][pc] == 1:
                    self.merge((r, c), (pr, pc), Parent, isLeft, isRight)

            if isLeft[r][c] and isRight[r][c]:
                ans = i + 1
                break
        return ans

if __name__ == '__main__':
    pass