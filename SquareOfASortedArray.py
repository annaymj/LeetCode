A1 = [-4,-1,0,3,10]

class Solution:
    '''
    Time Complexity: O(NlogN)
    Space Complexity: O)N
    '''
    def sortedSquares(self, A):
     
        A_square = [i*i for i in A]
        A_square = sorted(A_square)
        return A_square
      
    def sortedSquares2(self, A):
        return sorted(x*x for x in A)
      
    '''
    Time Complexity: O(N)
    Space Complexity: O(N)
    '''
    def sortedSquares3(self,A):
        N = len(A)
        # i, j: negative and postive index
        j = 0
        while j < N and A[j] < 0:
          j+= 1
        i = j-1
        
        ans = []
        while 0 <= i and j < N:
          if A[i] ** 2 < A[j] ** 2:
            ans.append(A[i] ** 2)
            i-=1
          else:
            ans.append(A[j] ** 2)
            j+=1
        
         #for remaining numbers
          while i>=0:
            ans.append(A[i] **2)
            i -=1
          while j<N:
            ans.append(A[j] **2)
            j +=1
          
          return ans
      
      
      
      
S = Solution()
S.sortedSquares(A1)
S.sortedSquares2(A1)
S.sortedSquares3(A1)