S1 = "(()())(())"
S2 = "(()())(())(()(()))"
S3 = "()()"

class Solution:
    def removeOuterParentheses(self, S):
      result=[]
      i,j = 0,1
      while j <= len(S):
        if self.validParenthesis(S[i:j]):
          result.append(S[i+1:j-1])
          
          #update i, j
          i = j
        j+=1
      return "".join(result)
    
    def validParenthesis(self,S):
      left,right = 0, 0
      for char in S:
        if char == "(":
          left += 1
        if char == ")":
          right +=1
          
      if left == right and left!=0:
        return True
      return False
          
          
S = Solution()
S.removeOuterParentheses(S1)
S.removeOuterParentheses(S2)
S.removeOuterParentheses(S3)