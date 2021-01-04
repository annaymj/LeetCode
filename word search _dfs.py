```
Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
```


ADJ = [(-1,0), (1,0), (0,-1),(0,1)]

class Solution:
    def search(self, board, row, col, word, visited):
        # base case: done when string is empty
        if len(word) == 0:
            return True
        
        # set current row and col as visited
        visited[row][col] = True
        
        # recursive rule: try stepping to each of the 4 neighbours, if the letter on that cell matches
        for dr, dc in ADJ:
            next_row = row + dr
            next_col = col + dc
            
            # check board bounds
            if 0 <= next_row < self._m and 0<= next_col < self._n:
                # check for letter match
                if board[next_row][next_col] == word[0] and not visited[next_row][next_col]:
                    result = self.search(board, next_row, next_col, word[1:],visited)
                    
                    if result == True:
                        return True
       
        # unmark current row col as visited if no solution is found
        visited[row][col] = False 
        
        # if we've exhausted all neighbours, report failure
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        self._m = len(board)
        self._n = len(board[0])
     
        # initiate emptry matrix filled with False for visited for each entry 
        visited = [[False] * self._n for _ in range(self._m)]
        
        for r in range(self._m):
            for c in range(self._n):
                if board[r][c] == word[0]: # first find the first matching word
                    if self.search(board, r, c, word[1:],visited): # then recursively search for the remaining words
                        return True
        return False
        
