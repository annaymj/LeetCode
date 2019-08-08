moves = "UD"

class Solution:
    def judgeCircle(self, moves):
        if len(moves)%2 != 0:
            return False
        
        if "U" in moves and "D" not in moves:
            return False
        elif ("U" or "D" in moves) and moves.count("U") != moves.count("D"):
            return False
        elif "L" in moves and "R" not in moves:
            return False
        elif ("L" or "R" in moves) and moves.count("L") != moves.count("R"):
            return False
        return True
      
    def judgeCircle2(self,moves):
        x = y = 0
        
        for move in moves:
          if move == 'U':
            y+=1
          elif move == 'D':
            y-=1
          elif move == 'L':
            x -=1
          elif move == 'R':
            x +=1
          
        return x == y == 0
      
  
  S=Solution()
  S.judgeCircle(moves)
  S.judgeCircle2(moves)