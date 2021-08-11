class Solution:
    def checkLineLegal(self, line):
        if len(line) < 3:
            return False

        for color in line:
            if color == '.':
                return False

        if line[0] != line[-1]:
            return False    
        
        for i in range(1, len(line) - 1):
            if line[i] == line[0]:
                return False

        return True

    def isValid(self, board, i, j):
        x = len(board)
        y = len(board[0])
        return (0 <= i < x) and (0 <= j < y)
        

    def checkMove(self, board, rMove: int, cMove: int,
                  color: str) -> bool:
        board[rMove][cMove] = color
        dxs = [0, 1, 0, -1, -1, 1, 1, -1]
        dys = [1, 0, -1, 0, -1, -1, 1, 1]

        for dx, dy in zip(dxs, dys):
            line = []
            for step in range(len(board)):
                endx = rMove + dx * step 
                endy = cMove + dy * step
                if not self.isValid(board, endx, endy):
                    break
                
                line.append(board[endx][endy])
                if self.checkLineLegal(line):
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    boards = [[[".", ".", ".", "B", ".", ".", ".", "."],
               [".", ".", ".", "W", ".", ".", ".", "."],
               [".", ".", ".", "W", ".", ".", ".", "."],
               [".", ".", ".", "W", ".", ".", ".", "."],
               ["W", "B", "B", ".", "W", "W", "W", "B"],
               [".", ".", ".", "B", ".", ".", ".", "."],
               [".", ".", ".", "B", ".", ".", ".", "."],
               [".", ".", ".", "W", ".", ".", ".", "."]],
              [[".", ".", ".", ".", ".", ".", ".", "."],
               [".", "B", ".", ".", "W", ".", ".", "."],
               [".", ".", "W", ".", ".", ".", ".", "."],
               [".", ".", ".", "W", "B", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", "B", "W", ".", "."],
               [".", ".", ".", ".", ".", ".", "W", "."],
               [".", ".", ".", ".", ".", ".", ".", "B"]]]
    rmoves = [4, 4]
    cmoves = [3, 4]
    colors = ['B', 'W']
    for board, rmove, cmove, color in zip(boards, rmoves, cmoves, colors):
        print(sol.checkMove(board, rmove, cmove, color))