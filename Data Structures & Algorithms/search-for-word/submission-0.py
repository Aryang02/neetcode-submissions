class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def check(i, j, idx):
            if idx == len(word):
                return True
            if not (0<=i<len(board)) or not (0<=j<len(board[0])):
                return False
            if board[i][j] != word[idx]:
                return False
            board[i][j] = '#'
            for dr, dc in directions:
                r, c = i+dr, j+dc
                if check(r, c, idx+1):
                    return True
            board[i][j] = word[idx]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and check(i, j, 0):
                    return True
        
        return False
