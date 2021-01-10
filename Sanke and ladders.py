```
On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board, and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:

You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:

You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations, regardless of the size of the board.)
If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].

Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.)

Return the least number of moves required to reach square N*N.  If it is not possible, return -1.

Example 1:
Input: [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output: 4

Explanation: 
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
```

from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self._m = len(board)
        target = self._m * self._m
        res = {1:0} #use a dictionary to store result, key is the number, value is the min number of moves
        
        queue = deque([1])
        
        while len(queue) > 0:
            n1 = queue.popleft()
            if n1 == target:
                print(res)
                return res[n1]
            
            n_min = n1 + 1
            n_max = min(n1 + 6, target)
            
            for n2 in range(n_min, n_max+1,1):
                r, c = self.get_boardrc(n2,self._m) # get row and col indexes
                
                if board[r][c] != -1: # if not at ladder/snake
                    n2 = board[r][c] # update the new board entry number
                    
                if n2 not in res:
                    res[n2] = res[n1] + 1 # update one move
                    queue.append(n2)
        return -1
        
    
    
    def get_boardrc(self, number, n):
        q,r = divmod(number-1, n) # get quotient and remainder of the division
        row_index = n - q - 1 # the row_index can be derived using m - quotient - 1
        
        if row_index % 2 == n % 2: # n and row index are both odd or even
            col_index = n - r - 1  # large number to small number
        else: # odd number
            col_index = r          # small number to large number
        
        return row_index, col_index # return row and col index
        
            
        
